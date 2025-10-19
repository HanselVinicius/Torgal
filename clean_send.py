from service.create_output_command_service import CreateOutputCommand
from service.perform_output_service import PerformOutputService
from utils.get_minio_data import get_of_minio
import pandas as pd
from fsutil import list_files,list_dirs
from domain.df_type import DfType
from dotenv import load_dotenv

load_dotenv()


def main():
    #get_of_minio()
    dirs = list_dirs('data/downloads')
    for index, dir in enumerate(dirs):
        files = list_files(dir)
        df = pd.read_csv('./' + files[0],low_memory=False)
        execute_output_command(index,df)
        
        

def execute_output_command(index,df):
    perform_output_service = PerformOutputService()
    if index == 0:
        createOutputCommand = CreateOutputCommand(df,perform_output_service,DfType.MANAGE_COMPLEXITY)
        createOutputCommand.execute()
    
    if index == 1:
        createOutputCommand = CreateOutputCommand(df,perform_output_service,DfType.TEACHER_REGULARITY)
        createOutputCommand.execute()

    if index == 2:
        createOutputCommand = CreateOutputCommand(df,perform_output_service,DfType.TEACHER_TRAINING)
        createOutputCommand.execute() 

if __name__ == "__main__":
    main()
