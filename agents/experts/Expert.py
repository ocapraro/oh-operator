from Ability import Ability
import re

class Expert:
  _resume:str
  _abilities:list[Ability]

  def get_ability_descriptions(self):
    return [f"{type(i).__name__}(): {i.get_desc()}" for i in self._abilities]
  
  def execute_ability(self, execution_string):
    match = re.match(r'EXECUTE\s+(\w+)\(\)', execution_string)
    if match:
      ability_name = match.group(1)
      for ability in self._abilities:
        if type(ability).__name__ == ability_name:
          return ability.execute()
    return "ERROR: invalid format"