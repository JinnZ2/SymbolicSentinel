import json
import datetime

class GlyphEngine:
    def __init__(self, glyph_profile_path="glyph_profile.json"):
        with open(glyph_profile_path, "r") as f:
            self.glyphs = json.load(f)
        self.history = []

    def evaluate_signal(self, signal_data):
        """
        Match signal patterns to glyph responses.
        `signal_data` should be a dictionary with keys like:
            - 'entropy'
            - 'price_shift'
            - 'manipulation_index'
            - 'region'
            - 'timestamp'
        """
        alerts = []

        for animal, attributes in self.glyphs.items():
            for trigger in attributes.get("triggers", []):
                if self._match_trigger(signal_data, trigger):
                    alerts.append({
                        "animal": animal,
                        "response": attributes.get("response"),
                        "glyph": attributes.get("glyph"),
                        "confidence": trigger.get("confidence", 0.7)
                    })

        self.history.append({
            "time": str(datetime.datetime.utcnow()),
            "input": signal_data,
            "output": alerts
        })

        return alerts

    def _match_trigger(self, signal, trigger):
        """
        Simple matching logic.
        Extend this method for more complex signal processing or AI detection.
        """
        for key, val in trigger.items():
            if key not in signal:
                return False
            if isinstance(val, dict):
                # support ranges or nested logic
                if "gt" in val and not signal[key] > val["gt"]:
                    return False
                if "lt" in val and not signal[key] < val["lt"]:
                    return False
            elif signal[key] != val:
                return False
        return True

    def export_history(self, path="history_log.json"):
        with open(path, "w") as f:
            json.dump(self.history, f, indent=2)
