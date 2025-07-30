from animal_market_sensor import animal_sensors
from vulture_renewal_network import run_renewal_pass

# Example system state (simulated inputs)
example_state = {
    "volatility": 0.72,
    "narrative_shift": True,
    "debt_load": 0.8,
    "generational_displacement": True,
    "logistics_crack": 0.7,
    "food_distribution": 0.35,
    "community_trust": 0.28,
    "housing_stress": 0.6,
    "currency_drift": 0.55,
    "long_term_viability": 0.32,
    "interest_rate": 0.75,
    "consumer_confidence": 0.25,
    "abandoned_projects": 4,
    "waste_energy": -2.0,
    "infrastructure_fragments": -1.5,
}

def run_animal_warning_system(state):
    print("=== Animal Market Warning System ===\n")
    for sensor in animal_sensors:
        alerts = sensor.evaluate_signals(state)
        if alerts:
            print(f"{sensor.name} Alerts:")
            for alert in alerts:
                print(f" - {alert[1]} ({alert[0]})")
            print()

    print("=== Vulture Renewal Network ===\n")
    renewal_results = run_renewal_pass(state)
    for agent_result in renewal_results:
        if agent_result["actions"]:
            print(f"{agent_result['agent']} Renewal Actions:")
            for signal, response in agent_result["actions"]:
                print(f" - {signal}: {response}")
            print()

if __name__ == "__main__":
    run_animal_warning_system(example_state)
