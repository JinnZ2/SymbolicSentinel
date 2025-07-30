# animal_modules/hyena.py
class Hyena:
    name = "Hyena"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("volatility", 0) > 0.75 and state.get("consumer_confidence", 1) < 0.4:
            alerts.append("Fracture-pounce behavior triggered — opportunistic rebalancing.")
        return alerts
