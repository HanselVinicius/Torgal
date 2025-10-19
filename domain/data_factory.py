
from domain.df_type import DfType
from domain.manage_complexity import ManageComplexity
from domain.teacher_regularity import TeacherRegularity
from domain.teacher_training.teacher_training import TeacherTraining


def create_from_row(dfType:DfType,row):
    match dfType:
        case DfType.TEACHER_TRAINING:
            return TeacherTraining.from_row(row)
        case DfType.MANAGE_COMPLEXITY:

            return ManageComplexity(
                adminitrative_dependencie=row['Unnamed: 8'],
                complexity_level=row['Unnamed: 9'],
                school_name=row['Unnamed: 6'],
                city=row['Unnamed: 4']
            )
        case DfType.TEACHER_REGULARITY:

            return TeacherRegularity(
                adminitrative_dependencie= row['Unnamed: 8'],
                average_regularity=row['Unnamed: 9'],
                school_name=row['Unnamed: 6'],
                city=row['Unnamed: 4']
                )