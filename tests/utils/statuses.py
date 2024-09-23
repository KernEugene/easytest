from enum import Enum


class TruckStatus(Enum):
    AVAILABLE = "Available"
    EN_ROUTE = "En route"
    NOT_AVAILABLE = "Not available"
    SELECT_ALL = "Select All"
