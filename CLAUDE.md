# CLAUDE.md — SymbolicSentinel

## Project Overview

SymbolicSentinel is an AI-guided early warning system for detecting systemic collapse (economic, ecological, energetic) using animal intelligence metaphors and symbolic glyph logic. It evaluates system state through biomimetic "animal sensor" agents that each monitor specific signals and trigger alerts when thresholds are crossed.

**Core mission:** "To warn, not to profit. To preserve memory, not to erase it. To re-seed life when collapse nears."

## Tech Stack

- **Language:** Python 3 (pure stdlib — no external dependencies)
- **Libraries:** `json`, `datetime`, `tkinter` (all standard library)
- **Config format:** JSON
- **License:** MIT

## Repository Structure

```
├── main.py                    # Primary entry point — runs warning system with example state
├── sentinel_engine.py         # SymbolicSentinel class — loads config and runs animal sensors
├── gui_launcher.py            # Tkinter GUI launcher (loads config.json, runs analysis)
├── animal_market_sensor.py    # AnimalSensor class + predefined sensor instances (Raven, Elephant, etc.)
├── animal_sensors_core.py     # Core sensor orchestration
├── vulture_renewal_network.py # Post-collapse regenerative agents (Vulture, Carrion Beetle, Hyena)
├── cycle_initiators.py        # Rebirth cycle detection (Butterfly, Spider, Frog, Owl, Turtle)
├── glyph_engine.py            # Glyph interpretation engine
├── market_warning_system.py   # Market warning system
├── config.json                # User-configurable system state input values
├── collapse_profiles.json     # Historical collapse profiles (2008 crisis, 2025 stress test)
├── .fieldlink.json            # Links to external BioGrid2.0 atlas repository
├── animal_modules/            # Individual animal behavior modules
│   ├── init.py                # Loads: Raven, Elephant, Vulture, CarrionBeetle, Hyena
│   ├── raven.py, elephant.py, spider.py, owl.py, frog.py
│   ├── ant.py, bee.py, whale.py, hyena.py
│   ├── vulture.py, carrion_beetle.py
├── data/                      # Tri-Invert Bridge seed and glyph JSON data
├── schema/                    # JSON Schema definitions (shape.seed.schema.json)
└── docs/                      # Extended documentation (tri_invert_bridge.md)
```

## Running the Project

```bash
# Run the warning system with example state
python3 main.py

# Run with GUI
python3 gui_launcher.py
```

Edit `config.json` to change input state values before running.

## Architecture & Key Patterns

### Animal Sensor Pattern

Every animal sensor follows the same interface:

```python
class AnimalSensor:
    def evaluate_signals(self, system_state: dict) -> list[tuple]:
        # Returns list of (signal_name, alert_message) tuples
```

Trigger logic uses threshold conditions:
- `{"gt": value}` — triggers when signal exceeds threshold
- `{"lt": value}` — triggers when signal falls below threshold
- `True`/`False` — triggers on exact boolean match

### Two Entry Paths

1. **`animal_market_sensor.py`** → defines `animal_sensors` list (Raven, Elephant, Ant, Wolf, Whale, Canary) used by `main.py`
2. **`sentinel_engine.py`** → `SymbolicSentinel` class loads `animal_modules/` via `load_all_animals()` (Raven, Elephant, Vulture, CarrionBeetle, Hyena)

### Three Agent Categories

| Category | Modules | Purpose |
|---|---|---|
| **Warning Agents** | Raven, Elephant, Ant, Wolf, Whale, Canary, Spider, Owl, Frog, Bee | Detect collapse signals |
| **Renewal Agents** | Vulture, Carrion Beetle, Hyena | Post-collapse scavenging and rebuilding |
| **Cycle Initiators** | Butterfly, Spider, Frog, Owl, Turtle | Detect rebirth thresholds |

### System State

The system state is a flat dictionary with numeric (0.0–1.0 scale or negative for decay) and boolean values:

```
volatility, narrative_shift, debt_load, generational_displacement,
logistics_crack, food_distribution, community_trust, housing_stress,
currency_drift, long_term_viability, interest_rate, consumer_confidence,
abandoned_projects, waste_energy, infrastructure_fragments
```

## Code Conventions

- **No external dependencies** — keep everything in Python stdlib
- **Class-per-animal pattern** in `animal_modules/` — each file exports one class with a `name` attribute and `evaluate_signals(state)` method
- **Simple, flat module structure** — no deep nesting
- **JSON for all configuration and data** — no YAML, TOML, or other formats
- **No formal test suite** — validation is done via example states in `main.py`
- **No linter/formatter configuration** — follow existing code style (PEP 8-ish, simple)

## Adding a New Animal Module

1. Create `animal_modules/<animal_name>.py` with a class that has:
   - `name` class attribute (string)
   - `evaluate_signals(self, state)` method returning a list of alerts
2. Import and add the class to `animal_modules/init.py` in `load_all_animals()`
3. Optionally add an `AnimalSensor` instance to `animal_market_sensor.py`

## Symbolic / Glyph System

The project uses symbolic glyphs for state representation:
- `↻` — phase-shift / melt
- `⚖` — balance
- `🕸` — lattice / network density

The **Tri-Invert Bridge** (`docs/tri_invert_bridge.md`) is a core concept: dual-triangle geometry enabling reversible state translation between collapse and renewal.

## Git Conventions

- **Commit messages:** Simple imperative format — `Create <filename>` or `Update <filename>`
- **Branch naming:** `feature/<description>` or `claude/<description>`
- **Default branch:** `main`

## Important Notes for AI Assistants

- This project intentionally has **zero external dependencies**. Do not add pip packages.
- The project uses **metaphorical/symbolic naming** (animals, glyphs, collapse). Respect the domain language.
- `config.json` is user-facing — keep it simple and well-structured.
- The `animal_modules/init.py` file (not `__init__.py`) serves as the module loader.
- Two parallel sensor systems exist (`animal_market_sensor.py` and `animal_modules/`). Both are valid entry paths.
- Collapse profiles in `collapse_profiles.json` are historical reference data — preserve integrity.
