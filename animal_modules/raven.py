
# animal_modules/raven.py
class Raven:
    name = "Raven"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("currency_drift", 0) > 0.6:
            alerts.append("Detected potential narrative distortion in valuation systems.")
        if state.get("volatility", 0) > 0.8:
            alerts.append("Unusual chaos signature — symbolic indicators may be drifting.")
        return alerts
