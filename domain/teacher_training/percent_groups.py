from dataclasses import dataclass
import json


@dataclass
class PercentGroups:
    group_1: float
    group_2: float
    group_3: float
    group_4: float
    group_5: float

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4) 