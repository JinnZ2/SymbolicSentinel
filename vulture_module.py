
# vulture_module.py
class Vulture:
    name = "Vulture"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("resource_waste", 0) > 0.6:
            alerts.append("Viable energy waste detected — initiating recovery sweep.")
        if state.get("infrastructure_decay", 0) > 0.5:
            alerts.append("Collapse site detected — rebuilder agents alerted.")
        return alerts
