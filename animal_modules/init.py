# animal_modules/__init__.py
from .raven import Raven
from .elephant import Elephant
from .vulture import Vulture
from .carrion_beetle import CarrionBeetle
from .hyena import Hyena

def load_all_animals():
    return [Raven(), Elephant(), Vulture(), CarrionBeetle(), Hyena()]
