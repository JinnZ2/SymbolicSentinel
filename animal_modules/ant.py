# animal_modules/ant.py
class Ant:
    name = "Ant"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("supply_chain_fragility", 0) > 0.6:
            alerts.append("Colony logistics unstable — triggering decentralized reroute.")
        if state.get("task_distribution_imbalance", 0) > 0.7:
            alerts.append("Role distortion detected — initiating adaptive division of labor.")
        return alerts
