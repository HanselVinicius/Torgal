from dataclasses import dataclass
import json

@dataclass
class TeacherRegularity:
    adminitrative_dependencie:str
    average_regularity:str
    school_name:str
    city:str

        
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4) 