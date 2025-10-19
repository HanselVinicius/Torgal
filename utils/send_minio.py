import os
from minio import Minio
from dotenv import load_dotenv
import glob

load_dotenv()

client = Minio(os.getenv("MINIO_URL"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=True,
)


def send_to_minio(folder_path, object_name_prefix):
    bucket_name = os.getenv("MINIO_BUCKET_URL").split("/")[-2]
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)

    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    for csv_file in csv_files:
        object_name = f"{object_name_prefix}/{os.path.basename(csv_file)}"
        client.fput_object(bucket_name, object_name, csv_file)
        print(csv_file, "successfully uploaded as object", object_name, "to bucket", bucket_name)
