import pyowm
from pyowm.caches.lrucache import LRUCache


def get_our_weather(coordinates=None, cityname=None, id=None):
    API_key = 'afb077071af62fa3b00cb43e3eccbaf1'
    owm = pyowm.OWM(API_key=API_key)
    # Cache provider to be used
    cache = LRUCache()
    obs = None
    ans = None
    if coordinates:
        obs = owm.weather_at_coords(coordinates[0], coordinates[1])
    if cityname:
        obs = owm.weather_at_place(cityname)
    weather = obs.get_weather()
    return weather


if __name__ == "__main__":
    coords = (-0.107331, 51.503614)
    w = get_our_weather(coordinates=coords)
    wind = w.get_wind()
    print(wind)
    w.get_reference_time()  # get time of observation in GMT UNIXtime
    w.get_reference_time(timeformat='iso')  # ...or in ISO8601
    w.get_clouds()  # Get cloud coverage
    w.get_rain()  # Get rain volume
    w.get_snow()  # Get snow volume
    w.get_wind()  # Get wind degree and speed
    w.get_humidity()  # Get humidity percentage
    w.get_pressure()  # Get atmospheric pressure
    w.get_temperature()  # Get temperature in Kelvin
    w.get_temperature(unit='celsius')  # ... or in Celsius degs
    w.get_temperature('fahrenheit')  # ... or in Fahrenheit degs
    w.get_status()  # Get weather short status
    w.get_detailed_status()  # Get detailed weather status
    w.get_weather_code()  # Get OWM weather condition code
    w.get_weather_icon_name()  # Get weather-related icon name
    w.get_sunrise_time()  # Sunrise time (GMT UNIXtime or ISO 8601)
    w.get_sunset_time('iso')  # Sunset time (GMT UNIXtime or ISO 8601)
    print(vars(w))
    # for item in dir(w):
    w_dict = {}
    for attr in vars(w):
        # if attr.startswith('get_'):
            w_dict[attr] = str(getattr(w, attr))
            print('{}: {}'.format(attr,w_dict[attr]))
