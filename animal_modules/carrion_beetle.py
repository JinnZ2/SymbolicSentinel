# animal_modules/carrion_beetle.py
class CarrionBeetle:
    name = "Carrion Beetle"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("housing_stress", 0) > 0.85:
            alerts.append("Deep decay detected — initiating cleanup and nutrient recycling.")
        return alerts
