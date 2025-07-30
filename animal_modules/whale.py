
# animal_modules/whale.py
class Whale:
    name = "Whale"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("deep_memory_suppression", 0) > 0.6:
            alerts.append("Ancestral echo blocked — initiating memory surfacing.")
        if state.get("acoustic_distortion", 0) > 0.5:
            alerts.append("Signal distortion in longwave channels — initiating resonance correction.")
        return alerts
