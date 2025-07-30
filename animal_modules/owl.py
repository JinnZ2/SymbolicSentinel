# animal_modules/owl.py
class Owl:
    name = "Owl"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("signal_noise_ratio", 1) < 0.5:
            alerts.append("Truth obscured — activating symbolic night-vision filter.")
        if state.get("decision_blindness", 0) > 0.7:
            alerts.append("Wisdom void detected — prompting guidance layer.")
        return alerts
