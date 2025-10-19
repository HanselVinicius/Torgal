from dataclasses import dataclass
import json

from domain.teacher_training.elementary_school import ElementarySchool
from domain.teacher_training.percent_groups import PercentGroups
from utils.to_float import to_float


@dataclass
class TeachStages:
    early_education: PercentGroups
    elementary_school: ElementarySchool
    middle_school: PercentGroups
    eja: PercentGroups


    @staticmethod
    def from_row(row):

        return TeachStages(
            early_education=TeachStages.create_early_education(row),
            elementary_school=TeachStages.create_elementary_school(row),
            middle_school=TeachStages.create_middle_school(row),
            eja=TeachStages.create_eja(row),
        )

    @staticmethod
    def create_early_education(row):
        return PercentGroups(
            group_1=to_float(row["Unnamed: 10"]),
            group_2=to_float(row["Unnamed: 11"]),
            group_3=to_float(row["Unnamed: 12"]),
            group_4=to_float(row["Unnamed: 13"]),
            group_5=to_float(row["Unnamed: 14"]),
        )
        
    @staticmethod    
    def create_eja(row):
        return PercentGroups(
            group_1=to_float(row["Unnamed: 35"]),
            group_2=to_float(row["Unnamed: 36"]),
            group_3=to_float(row["Unnamed: 37"]),
            group_4=to_float(row["Unnamed: 38"]),
            group_5=to_float(row["Unnamed: 39"]),
        )
        
    @staticmethod            
    def create_elementary_school(row):
        def create_total():
            return PercentGroups(
                group_1=to_float(row["Unnamed: 15"]),
                group_2=to_float(row["Unnamed: 16"]),
                group_3=to_float(row["Unnamed: 17"]),
                group_4=to_float(row["Unnamed: 18"]),
                group_5=to_float(row["Unnamed: 19"]),
            )

        def create_initial_years():
            return PercentGroups(
                group_1=to_float(row["Unnamed: 20"]),
                group_2=to_float(row["Unnamed: 21"]),
                group_3=to_float(row["Unnamed: 22"]),
                group_4=to_float(row["Unnamed: 23"]),
                group_5=to_float(row["Unnamed: 24"]),
            )

        def create_final_years():
            return PercentGroups(
                group_1=to_float(row["Unnamed: 25"]),
                group_2=to_float(row["Unnamed: 26"]),
                group_3=to_float(row["Unnamed: 27"]),
                group_4=to_float(row["Unnamed: 28"]),
                group_5=to_float(row["Unnamed: 29"]),
            )

        return ElementarySchool(
            total=create_total(),
            initial_years=create_initial_years(),
            final_years=create_final_years(),
        )
        
        
    @staticmethod    
    def create_middle_school(row):
        return PercentGroups(
            group_1=to_float(row["Unnamed: 30"]),
            group_2=to_float(row["Unnamed: 31"]),
            group_3=to_float(row["Unnamed: 32"]),
            group_4=to_float(row["Unnamed: 33"]),
            group_5=to_float(row["Unnamed: 34"]),
        )

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4) 