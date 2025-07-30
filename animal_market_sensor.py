class AnimalSensor:
    def __init__(self, name, traits, signals_monitored, trigger_logic):
        self.name = name
        self.traits = traits
        self.signals_monitored = signals_monitored
        self.trigger_logic = trigger_logic

    def evaluate_signals(self, system_state):
        alerts = []
        for signal, condition in self.trigger_logic.items():
            value = system_state.get(signal)
            if value is None:
                continue
            if isinstance(condition, dict):
                if "gt" in condition and value > condition["gt"]:
                    alerts.append((signal, f"{self.name} detected high"))
                if "lt" in condition and value < condition["lt"]:
                    alerts.append((signal, f"{self.name} detected low"))
            elif value == condition:
                alerts.append((signal, f"{self.name} triggered"))
        return alerts


animal_sensors = [
    AnimalSensor(
        name="Raven",
        traits=["strategic observer", "shiny object follower", "unusual behavior detector"],
        signals_monitored=["volatility", "narrative_shift"],
        trigger_logic={
            "volatility": {"gt": 0.65},
            "narrative_shift": True
        }
    ),
    AnimalSensor(
        name="Elephant",
        traits=["long-memory", "early tremor detection", "migration mapper"],
        signals_monitored=["debt_load", "generational_displacement"],
        trigger_logic={
            "debt_load": {"gt": 0.75},
            "generational_displacement": True
        }
    ),
    AnimalSensor(
        name="Ant",
        traits=["infrastructure sensing", "underground signal", "coordinated retreat"],
        signals_monitored=["logistics_crack", "food_distribution"],
        trigger_logic={
            "logistics_crack": {"gt": 0.6},
            "food_distribution": {"lt": 0.4}
        }
    ),
    AnimalSensor(
        name="Wolf",
        traits=["pack coherence", "social fray sensing"],
        signals_monitored=["community_trust", "housing_stress"],
        trigger_logic={
            "community_trust": {"lt": 0.3},
            "housing_stress": {"gt": 0.5}
        }
    ),
    AnimalSensor(
        name="Whale",
        traits=["deep frequency listener", "ecosystem-wide perception"],
        signals_monitored=["currency_drift", "long_term_viability"],
        trigger_logic={
            "currency_drift": {"gt": 0.5},
            "long_term_viability": {"lt": 0.4}
        }
    ),
    AnimalSensor(
        name="Canary",
        traits=["sensitive micro-instability", "early entropy alarm"],
        signals_monitored=["interest_rate", "consumer_confidence"],
        trigger_logic={
            "interest_rate": {"gt": 0.7},
            "consumer_confidence": {"lt": 0.3}
        }
    )
]
