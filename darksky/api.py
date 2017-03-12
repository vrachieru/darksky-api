import requests
from .model import Forecast, Language, Units

class DarkSky:
    BASE_URL = 'https://api.darksky.net/forecast'

    def __init__(self, apikey):
        self.apikey = apikey

    def get(self, latitude, longitude, language=Language.ENGLISH, units=Units.AUTO):
        response = requests.get(self.build_url(latitude, longitude, language, units))
        return Forecast(response.json())

    def build_url(self, latitude, longitude, language, units):
        return '%s/%s/%s,%s?lang=%s&units=%s' \
            % (self.BASE_URL, self.apikey, latitude, longitude, language, units)
