import os
from minio import Minio
from dotenv import load_dotenv

load_dotenv() 

client = Minio(os.getenv("MINIO_URL"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=True,
)

def get_of_minio():
    bucket_name = os.getenv("MINIO_BUCKET_URL").split("/")[-2]
    objects = client.list_objects(bucket_name=bucket_name,recursive=True)
    download_dir = os.getenv("DOWNLOAD_DIR")  
    
    os.makedirs(download_dir, exist_ok=True)
    for obj in objects:
        object_name = obj.object_name
        local_path = os.path.join(download_dir, object_name)

        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        print(f"Baixando {object_name} para {local_path}...")
        client.fget_object(bucket_name, object_name, local_path)
        
get_of_minio()
    