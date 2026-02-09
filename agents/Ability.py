from abc import ABC, abstractmethod
import json

class Ability(ABC):
  _desc:str = ""
  _params = []
  _param_req_string = ""

  @abstractmethod
  def execute(self) -> str:
    pass

  def request_params(self) -> str:
    if self._param_req_string == "":
      return ""
    return f"I can help with that, I just need the following information in a JSON parsable array: {self._param_req_string}"

  def set_params(self, raw_params:str):
    self._params = json.loads(raw_params)

  def get_desc(self) -> str:
    return self._desc