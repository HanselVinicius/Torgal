import os
import json
import requests

from domain.manage_complexity import ManageComplexity
from domain.teacher_regularity import TeacherRegularity
from domain.teacher_training.teacher_training import TeacherTraining

class PerformOutputService:
    
    def __init__(self):
        self.api_url = os.getenv("RINOA_API_URL")
        self.secret = os.getenv("RINOA_API_SECRET", "dev_secret")
        if not self.api_url:
            raise ValueError("RINOA_API_URL not set in environment variables")

    def execute_manage_complexity_output(self, data: ManageComplexity):
        url = f"{self.api_url}/v1/manage-complexity"
        payload = {
            "adminitrative_dependencie": data.adminitrative_dependencie,
            "complexity_level": data.complexity_level,
            "school_name": data.school_name,
            "city": data.city,
            "secret": self.secret
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def execute_teacher_training_output(self, data: TeacherTraining):
        url = f"{self.api_url}/v1/teacher-training"
        payload = json.loads(data.teachStages.early_education.toJSON())
        payload = {
            "teach_stages": {
                "early_education": json.loads(data.teachStages.early_education.toJSON()),
                "elementary_school": {
                    "total": json.loads(data.teachStages.elementary_school.total.toJSON()),
                    "initial_years": json.loads(data.teachStages.elementary_school.initial_years.toJSON()),
                    "final_years": json.loads(data.teachStages.elementary_school.final_years.toJSON())
                },
                "middle_school": json.loads(data.teachStages.middle_school.toJSON()),
                "eja": json.loads(data.teachStages.eja.toJSON())
            },
            "adminitrative_dependencie": data.adminitrative_dependencie,
            "school_name": data.school_name,
            "city": data.city,
            "secret": self.secret
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def execute_teacher_regularity_output(self, data: TeacherRegularity):
        url = f"{self.api_url}/v1/teacher-regularity"
        payload = {
            "adminitrative_dependencie": data.adminitrative_dependencie,
            "average_regularity": data.average_regularity,
            "school_name": data.school_name,
            "city": data.city,
            "secret": self.secret
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
