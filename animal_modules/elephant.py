
# animal_modules/elephant.py
class Elephant:
    name = "Elephant"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("debt_load", 0) > 0.75:
            alerts.append("Heavy structural burden sensed — historical memory conflict.")
        if state.get("interest_rate", 0) > 0.7:
            alerts.append("Rate pressure triggering long-memory stability warnings.")
        return alerts
