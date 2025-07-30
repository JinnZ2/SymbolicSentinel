
# sentinel_engine.py
from animal_modules import load_all_animals
import json

class SymbolicSentinel:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            self.state = json.load(f)
        self.animals = load_all_animals()

    def run_sensors(self):
        results = {}
        for animal in self.animals:
            alerts = animal.evaluate_signals(self.state)
            if alerts:
                results[animal.name] = alerts
        return results
