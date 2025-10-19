from dataclasses import dataclass
import json
from domain.teacher_training.percent_groups import PercentGroups

@dataclass
class ElementarySchool:
    total: PercentGroups
    initial_years: PercentGroups
    final_years: PercentGroups
    
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4) 