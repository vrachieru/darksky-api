import sys
sys.path.append('../')

from darksky import DarkSky

darksky = DarkSky('YOUR_API_KEY')
forecast = darksky.get(47.2, 27.6)

print('Summary: %s' % forecast.currently.summary)
print('Temperature: %s*C, feels like %s*C' % (forecast.currently.temperature, forecast.currently.apparentTemperature))
