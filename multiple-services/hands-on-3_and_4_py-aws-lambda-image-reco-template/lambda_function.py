from keras.applications.mobilenet import MobileNet, decode_predictions, preprocess_input
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.models import load_model
from keras.preprocessing import image

import numpy as np

import boto3
from io import BytesIO
import json
import os

s3 = boto3.client('s3')
sns = boto3.client('sns')
model = MobileNet()

def lambda_handler(event, context):

    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        print('Reading {} from S3 bucket {}'.format(file_key, bucket_name))
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)

        s3Img = obj['Body'].read()
        img = image.load_img(BytesIO(s3Img), target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)   
        pImg = preprocess_input (img)

        preds = model.predict(pImg)
        prediction = decode_predictions(preds, top=1)[0][0]
        print(prediction)
        
        result = { "status": "ok", "name": file_key, "result": str(prediction[1]), "confidence": float(prediction[2]) }
        
        snsTopicArn = os.environ["snsTopicArn"]
        response = sns.publish(
                TargetArn=snsTopicArn,
                Message=json.dumps({'default': json.dumps(result)}),
                MessageStructure='json'
            )
        
        print(response)
    except Exception as e:
        print(e)
        raise e
    