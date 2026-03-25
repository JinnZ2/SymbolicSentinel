# animal_modules/__init__.py
from .raven import Raven
from .elephant import Elephant
from .vulture import Vulture
from .carrion_beetle import CarrionBeetle
from .hyena import Hyena
from .spider import Spider
from .owl import Owl
from .frog import Frog
from .ant import Ant
from .bee import Bee
from .whale import Whale

def load_all_animals():
    return [
        Raven(), Elephant(), Spider(), Owl(), Frog(),
        Ant(), Bee(), Whale(),
        Vulture(), CarrionBeetle(), Hyena()
    ]
