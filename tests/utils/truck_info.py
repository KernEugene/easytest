import random
from enum import Enum

class TruckInfo(Enum):
    UNIT = "1234511"
    DISPATCHER_NAME = "Tester Megaladon"
    DISPATCHER_PHONE = "123456789"
    DRIVER_NAME_1 = "Michael Schumacher"
    DRIVER_NAME_2 = "Ken Block"
    DRIVER_1_PHONE = "8238428348"
    DRIVER_2_PHONE = "4234243242"
    LENGTH = "100"
    WIDTH = "100"
    HEIGHT = "100"
    PAYLOAD = "1000"

    @classmethod
    def generate_random_unit(cls) -> str:
        return ''.join(random.choices('0123456789', k=6))