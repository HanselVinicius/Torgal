import json
from dataclasses import dataclass

@dataclass
class ManageComplexity:
    adminitrative_dependencie:str
    complexity_level:str
    school_name:str
    city:str

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4) 