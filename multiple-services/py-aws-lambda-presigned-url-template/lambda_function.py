import uuid

import boto3
import os
import json

# Get the service client.
s3 = boto3.client('s3')
   
def lambda_handler(event, context):
   
   # Retrieve the filename
   upload_key = event["queryStringParameters"]["filename"]

   # Generate the presigned URL for put requests
   presigned_url = s3.generate_presigned_post(
       Bucket = os.environ["bucketName"],
       Key = upload_key,
       ExpiresIn = 60
   )
   
   print(presigned_url)
   # Return the presigned URL
   return {
       "headers":{
          "Access-Control-Allow-Origin":"*"
       },
       "body": json.dumps(presigned_url)
   }