# animal_modules/frog.py
class Frog:
    name = "Frog"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("ecosystem_entropy", 0) > 0.5:
            alerts.append("Environmental imbalance detected — initiating regeneration hops.")
        if state.get("toxic_load", 0) > 0.6:
            alerts.append("Amphibian threshold crossed — toxic signal received.")
        return alerts
