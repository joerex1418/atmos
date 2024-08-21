import httpx

from .constants import NWS_BASE
from .constants import OSM_BASE
from .constants import OSM_REVERSE_BASE


def locate(city:str=None, state:str=None, zipcode:str=None, country:str="us") -> list[dict]:
    params = {
        "city": city,
        "state": state,
        "postalcode": zipcode,
        "country": country,
        "format": "jsonv2",
    }

    with httpx.Client() as client:
        r = client.get(OSM_BASE, params=params)
        return r.json()


def get_coordinates(city:str=None, state:str=None, zipcode:str=None, country:str="us") -> tuple[float, float]:
    location_data = locate(city, state, zipcode)
    lat = location_data[0]["lat"]
    lon = location_data[0]["lon"]
    return float(lat), float(lon) 





class Atmos:
    def __init__(self, lat, lon, **kwargs):
        params = {
            "lat": lat,
            "lon": lon,
            "unit": 0,
            "lg": "english",
            "FcstType": "json",
        }

        r = httpx.get(NWS_BASE, params=params)

        self.data = r.json()

