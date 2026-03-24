#!/usr/bin/env bash
# fieldlink-pull.sh — Fetch and stage remote ecosystem content into atlas/remote/
#
# Usage: ./fieldlink-pull.sh [mount-name]
#   No arguments: pulls all declared mounts
#   With argument: pulls only the named mount
#
# This script reads atlas/shapes.json for declared remote_mounts,
# clones or updates each repo into atlas/remote/<name>/.
# Designed for the BioGrid2.0 ecosystem — pure git, no dependencies.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ATLAS_SHAPES="$SCRIPT_DIR/atlas/shapes.json"
REMOTE_DIR="$SCRIPT_DIR/atlas/remote"

# ------------------------------------------------------------
# Lightweight JSON key reader (no jq dependency)
# Extracts simple string values from flat JSON objects
# ------------------------------------------------------------
json_value() {
    local file="$1" key="$2"
    python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    data = json.load(f)
for k in sys.argv[2].split('.'):
    data = data[k]
print(data)
" "$file" "$key" 2>/dev/null
}

json_keys() {
    local file="$1" path="$2"
    python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    data = json.load(f)
for k in sys.argv[2].split('.'):
    data = data[k]
for k in data:
    print(k)
" "$file" "$path" 2>/dev/null
}

# ------------------------------------------------------------
# Pull a single mount
# ------------------------------------------------------------
pull_mount() {
    local name="$1"
    local repo
    repo=$(json_value "$ATLAS_SHAPES" "remote_mounts.$name.repo")

    if [ -z "$repo" ]; then
        echo "  [skip] No repo URL found for mount: $name"
        return 1
    fi

    local target="$REMOTE_DIR/$name"
    mkdir -p "$target"

    if [ -d "$target/.git" ]; then
        echo "  [update] $name — pulling latest from $repo"
        git -C "$target" pull --ff-only origin main 2>/dev/null \
            || git -C "$target" pull --ff-only origin master 2>/dev/null \
            || echo "  [warn] Could not fast-forward $name — may need manual merge"
    else
        echo "  [clone] $name — cloning from $repo"
        # Clone into a temp dir then move contents (keeps atlas/remote/<name> as root)
        local tmpdir
        tmpdir=$(mktemp -d)
        if git clone --depth 1 "$repo" "$tmpdir" 2>/dev/null; then
            # Move repo contents into mount target
            rm -rf "$target"
            mv "$tmpdir" "$target"
            echo "  [ok] $name mounted at $target"
        else
            rm -rf "$tmpdir"
            echo "  [fail] Could not clone $repo — repo may not exist yet"
            echo "         Mount stub preserved at $target/.mount.json"
            return 1
        fi
    fi

    # Update mount status
    if [ -f "$target/.mount.json" ]; then
        python3 -c "
import json, sys
p = sys.argv[1]
with open(p, 'r') as f:
    data = json.load(f)
data['status'] = 'mounted'
with open(p, 'w') as f:
    json.dump(data, f, indent=2)
    f.write('\n')
" "$target/.mount.json" 2>/dev/null
    fi
}

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
echo "=== SymbolicSentinel Fieldlink Pull ==="
echo "Atlas shapes: $ATLAS_SHAPES"
echo ""

if [ ! -f "$ATLAS_SHAPES" ]; then
    echo "[error] atlas/shapes.json not found. Run from repo root."
    exit 1
fi

FILTER="${1:-}"

if [ -n "$FILTER" ]; then
    echo "Pulling mount: $FILTER"
    pull_mount "$FILTER"
else
    echo "Pulling all declared mounts..."
    echo ""
    for mount in $(json_keys "$ATLAS_SHAPES" "remote_mounts"); do
        pull_mount "$mount" || true
        echo ""
    done
fi

echo "=== Fieldlink pull complete ==="
