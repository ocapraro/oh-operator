from abilities import GetWeather
from Expert import Expert
class WeatherMan(Expert):
  _resume = "Hi I'm Weather Man! I have a whole bunch of weather sensors, so I can tell you what the weather is anywhere in the world."
  _abilities = [GetWeather()]
