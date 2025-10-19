from domain.data_factory import create_from_row
from domain.df_type import DfType
from service.perform_output_service import PerformOutputService


class CreateOutputCommand():
    
    def __init__(self,df,perform_output_service:PerformOutputService,dfType:DfType):
        self.df = df
        self.perform_output_service = perform_output_service
        self.dfType = dfType
    
    def execute(self):
        filtered_df = self._filter_df(self.df)
        self._traverse_outputting(filtered_df)
       
        
    def _filter_df(self,df):
        filtered_df = df[(df['Unnamed: 4'] == 'Sertãozinho')  & (df['Unnamed: 2'] == 'SP') ]
        return filtered_df
     
    def _traverse_outputting(self,df):
        for index, row in df.iterrows():
            data = create_from_row(self.dfType,row)
            self._execute_output(data)

    def _execute_output(self, data):
        if self.dfType == DfType.TEACHER_TRAINING:
            self.perform_output_service.execute_teacher_training_output(data)
            
        elif self.dfType == DfType.MANAGE_COMPLEXITY:
            self.perform_output_service.execute_manage_complexity_output(data)
        
        elif self.dfType == DfType.TEACHER_REGULARITY:
            self.perform_output_service.execute_teacher_regularity_output(data)
