from boto3 import client
import logging
from botocore.exceptions import ClientError
from os import getenv
                
def upload_file(file_name, object_name=None):
    bucket_name= getenv('S3_BUCKET_NAME', default=None)
    if object_name is None:
        object_name = file_name

    s3_client = client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return e

    return get_temp_url(file_name, bucket_name)

def get_temp_url(object_key, bucket_name):
    s3_client = client('s3')
    try:
        url= s3_client.generate_presigned_url(
    ClientMethod='get_object', 
    Params={'Bucket': bucket_name, 'Key': object_key},
    ExpiresIn=3600)
        return str(url)
    except ClientError as e:
        return e
