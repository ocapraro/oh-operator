from Ability import Ability
import requests

class GetWeather(Ability):
  CITIES = {
    "sanFrancisco": "https://api.weather.gov/gridpoints/MTR/85,105/forecast",
    "newYork":       "https://api.weather.gov/gridpoints/OKX/33,36/forecast",
    "losAngeles":    "https://api.weather.gov/gridpoints/LOX/93,97/forecast",
    "lasVegas":      "https://api.weather.gov/gridpoints/VEF/70,78/forecast",
    "chicago":       "https://api.weather.gov/gridpoints/LOT/61,55/forecast"
  }

  _desc = "Gets the current weather in a specific city"
  _param_req_string = f"city(choose one of {[i for i,_ in CITIES.keys()]})"

  
  def execute(self):
    city = self._params[0]
    try:
      res = requests.get(self.CITIES[city])
      res.raise_for_status() 
      data = res.json()

    except Exception:
      return "ERROR: Failed to get weather data"

    return f"{data}"