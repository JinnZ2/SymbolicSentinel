
# animal_sensors_core.py
from raven_module import Raven
from vulture_module import Vulture
from animal_modules.elephant import Elephant
from animal_modules.spider import Spider
from animal_modules.owl import Owl
from animal_modules.frog import Frog
from animal_modules.hyena import Hyena
from animal_modules.carrion_beetle import CarrionBeetle
from animal_modules.whale import Whale
from animal_modules.bee import Bee
from animal_modules.ant import Ant

animal_agents = [
    Raven(), Vulture(), Elephant(), Spider(), Owl(), Frog(),
    Hyena(), CarrionBeetle(), Whale(), Bee(), Ant()
]

def run_animal_sensors(system_state):
    all_alerts = {}
    for agent in animal_agents:
        agent_alerts = agent.evaluate_signals(system_state)
        if agent_alerts:
            all_alerts[agent.name] = agent_alerts
    return all_alerts
