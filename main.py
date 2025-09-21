from pyspark.sql import SparkSession
import glob
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv() 

EXCEL_FILE_PATH = os.getenv("EXCEL_FILE_PATH")

def append_dataframes():
    excels = glob.glob(EXCEL_FILE_PATH)
    result = []
    for file in excels:
        df = pd.read_excel(file)
        df['filename'] = file
        result.append(df)
    return result

def convert_to_spark_df(pandas_df,spark):
    spark_dfs = []
    merged_df = None
    for df_p in pandas_df:
        spark_dfs.append(spark.createDataFrame(df_p))

    if spark_dfs:
        merged_df = spark_dfs[0]
        for i in range(1, len(spark_dfs)):
            merged_df = merged_df.union(spark_dfs[i])
    return merged_df

def to_csv(spark_df, output_path):
    if spark_df:
        spark_df.coalesce(1).write.option("header", "true").csv(output_path)
        

def main():
    spark = SparkSession.builder.appName("MergeExcelFiles").getOrCreate()
    merged_df = append_dataframes()
    spark_df = convert_to_spark_df(merged_df,spark)
    to_csv(spark_df, "./merged.csv")
    print('writed')

    
if __name__ == "__main__":
    main()
