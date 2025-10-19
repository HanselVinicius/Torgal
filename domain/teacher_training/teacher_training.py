from dataclasses import dataclass
import json

from domain.teacher_training.teach_stages import TeachStages


@dataclass
class TeacherTraining:
    teachStages:TeachStages
    adminitrative_dependencie:str
    school_name:str
    city:str
    
    @staticmethod
    def from_row(row):
        
        return TeacherTraining(
            teachStages= TeachStages.from_row(row),
            adminitrative_dependencie= row['Unnamed: 8'],
            school_name= row['Unnamed: 6'],
            city=row['Unnamed: 4']
        )
        

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4) 