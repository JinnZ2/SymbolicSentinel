
# animal_modules/spider.py
class Spider:
    name = "Spider"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("network_fragility", 0) > 0.6:
            alerts.append("Web disruption detected — activating reweaving protocol.")
        if state.get("social_disconnection", 0) > 0.7:
            alerts.append("Signal thread thinning — social bonds need repair.")
        return alerts
