
# animal_modules/bee.py
class Bee:
    name = "Bee"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("pollination_breakdown", 0) > 0.6:
            alerts.append("Mutualistic collapse — warning: decentralized systems at risk.")
        if state.get("overcentralization", 0) > 0.7:
            alerts.append("Hive structure imbalance — recommend swarm logic restoration.")
        return alerts
