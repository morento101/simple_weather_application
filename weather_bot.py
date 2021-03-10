from pyowm.owm import OWM
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'ua'  # your language here, eg. Ukrainian
owm = OWM('56f421978ffb55c1a00b762ac54d6ce4', config_dict)
mgr = owm.weather_manager()


place = input('Введіть ваше місто: ')
observation = mgr.weather_at_place(place)
w = observation.weather


temp = w.temperature('celsius')
temp_current = temp['temp']
temp_min = temp['temp_min']
temp_max = temp['temp_max']
feels_like = temp['feels_like']

print('Температура зараз: ' + str(temp_current) + '\nМінімальна температура сьогодні: ' + str(temp_min) + ' градуси')
print('Максимальна температура сьогодні: ' + str(temp_max) + ' градуси'
      '\nВідчувається як: ' + str(feels_like) + ' градуси')


wind_info = observation.weather.wind(unit='meters_sec')
wind_speed = wind_info['speed']
wind_deg = wind_info['deg']

print('Швидкість вітру сьогодні ' + str(wind_speed) + ' метра за секунду'
      '\nНапрям вітру у градусах від північного горизонту: ' + str(wind_deg))
