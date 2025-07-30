# animal_modules/vulture.py
class Vulture:
    name = "Vulture"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("consumer_confidence", 1) < 0.3:
            alerts.append("Detected decline — potential opportunity scavenging underway.")
        if state.get("housing_stress", 0) > 0.7:
            alerts.append("Decaying assets — energy scavenging behavior triggered.")
        return alerts
