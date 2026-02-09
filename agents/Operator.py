from Agent import Agent
from experts.Expert import Expert
from experts.weather_man.WeatherMan import WeatherMan
class Operator(Agent):
  _contacts:list[Expert]

  def __init__(self, contacts:list[Expert]) -> None:
    self._contacts = contacts
    self._initial_prompt="You are an Operator for a Expert Service, a service that connects people with experts to help with their problems. Whenever you are asked a question you must determine if an expert is required or if a generalist can handle it. Respond in the format {decision:\"generalist\"||EXPERT_NAME}. Here are your experts:\n"+"\n".join([str(c) for c in contacts])
    self._initial_response="{decision:\"generalist\"}"


op = Operator([WeatherMan()])

print(op.get_initial_prompt())