
# market_warning_system.py
from animal_sensors_core import run_animal_sensors

def simulate_market_state(state):
    print("Simulating market warning system...")
    alerts = run_animal_sensors(state)
    for animal, messages in alerts.items():
        print(f"[{animal}]")
        for msg in messages:
            print(f"  - {msg}")
    return alerts

if __name__ == "__main__":
    # Example synthetic state input
    test_state = {
        "pattern_shift_score": 0.75,
        "information_distortion": 0.68,
        "resource_waste": 0.7,
        "infrastructure_decay": 0.6,
        "deep_memory_suppression": 0.65,
        "pollination_breakdown": 0.66,
        "supply_chain_fragility": 0.72
    }
    simulate_market_state(test_state)
