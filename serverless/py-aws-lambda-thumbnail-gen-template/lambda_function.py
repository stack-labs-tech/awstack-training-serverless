import PIL
from PIL import Image
from io import BytesIO
import os
import ast

import boto3


s3 = boto3.client('s3')

def lambda_handler(event, context):

    message = ast.literal_eval(event['Records'][0]['Sns']['Message'])
    bucket_name = os.environ["imgSrcBucket"]
    thumb_bucket = os.environ["thumbDestBucket"]
    
    print('Processing SNS message {} '.format(message))
    
    # Downloading the image from the S3 image bucket
    file_key = message['name']
    tmp_filename = '/tmp/' + os.path.basename(file_key) 
    s3.download_file(Bucket=bucket_name, Key=file_key, Filename=tmp_filename)

    img = Image.open(tmp_filename)
    
    # Resizing the image
    img.thumbnail((128, 128), PIL.Image.ANTIALIAS)
    dest_thumb = tmp_filename + "_thumb." + img.format
    img.save(dest_thumb)

    # Uploading the image to the S3 thumbnail bucket
    s3.upload_file(Filename=dest_thumb, Bucket=thumb_bucket, Key=file_key)

    # Printing to CloudWatch
    print('File saved at {}/{}'.format(
        thumb_bucket,
        file_key,
    ))

