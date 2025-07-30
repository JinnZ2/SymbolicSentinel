class RenewalAgent:
    def __init__(self, name, traits, specialization, actions):
        self.name = name
        self.traits = traits
        self.specialization = specialization
        self.actions = actions

    def scavenge_opportunities(self, system_state):
        results = []
        for signal, value in system_state.items():
            if isinstance(value, (int, float)) and value < 0:
                results.append((signal, "salvageable anomaly"))
            elif "waste" in signal or "abandoned" in signal:
                results.append((signal, "repurpose"))
        return results

# Vulture-based regenerative agents
vulture_network = [
    RenewalAgent(
        name="Vulture",
        traits=["thermal soaring", "crisis scavenger", "high-altitude scout"],
        specialization="detecting collapse zones and systemic leftovers",
        actions=["search ruins", "salvage infrastructure", "map collapse edge"]
    ),
    RenewalAgent(
        name="Carrion Beetle",
        traits=["biological decay mapper", "nutrient recycler"],
        specialization="micro-layer cleanup and reuse",
        actions=["recycle code", "digest broken structures", "return value to soil"]
    ),
    RenewalAgent(
        name="Hyena",
        traits=["pack coordination", "bone cracker", "laughter signaling"],
        specialization="recovering hidden strength in collapse",
        actions=["test resilience remnants", "alert scavenger allies"]
    )
]

def run_renewal_pass(system_state):
    results = []
    for agent in vulture_network:
        results.append({
            "agent": agent.name,
            "actions": agent.scavenge_opportunities(system_state)
        })
    return results
