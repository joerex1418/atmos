import rich
from src.api import locate
from src.api import get_coordinates
from src.api import Atmos


coords = get_coordinates(zipcode=60013)

atmos = Atmos(coords[0], coords[1])

rich.print(atmos.data)