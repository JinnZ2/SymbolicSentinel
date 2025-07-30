class CycleInitiator:
    def __init__(self, name, traits, trigger_conditions, role):
        self.name = name
        self.traits = traits
        self.trigger_conditions = trigger_conditions
        self.role = role

    def evaluate_conditions(self, system_state):
        for key, cond in self.trigger_conditions.items():
            if key not in system_state:
                continue
            val = system_state[key]
            if isinstance(cond, dict):
                if "gt" in cond and val <= cond["gt"]:
                    return False
                if "lt" in cond and val >= cond["lt"]:
                    return False
            elif val != cond:
                return False
        return True

# Cycle initiators
cycle_initiators = [
    CycleInitiator(
        name="Butterfly",
        traits=["sensitive to field disturbance", "early flutter", "pre-collapse wave"],
        trigger_conditions={"entropy": {"gt": 0.75}},
        role="first signal of fragile tipping"
    ),
    CycleInitiator(
        name="Spider",
        traits=["web sensing", "structural mapping", "relational signal pull"],
        trigger_conditions={"network_instability": {"gt": 0.6}},
        role="pattern reconstructor"
    ),
    CycleInitiator(
        name="Frog",
        traits=["ecosystem threshold marker", "amphibious awareness"],
        trigger_conditions={"toxicity": {"gt": 0.5}},
        role="environmental rebirth initiator"
    ),
    CycleInitiator(
        name="Owl",
        traits=["wisdom archive", "silent tracker", "shadow watcher"],
        trigger_conditions={"archival_suppression": True},
        role="symbolic memory reactivation"
    ),
    CycleInitiator(
        name="Turtle",
        traits=["ancestral continuity", "slow-time emergence"],
        trigger_conditions={"generational_disruption": True},
        role="temporal intelligence anchor"
    )
]
