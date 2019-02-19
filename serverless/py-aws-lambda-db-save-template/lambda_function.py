import boto3
import json
import uuid
import datetime

import ast
import os

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):

    try:
        message = ast.literal_eval(event['Records'][0]['Sns']['Message'])

        print('Processing SNS message {} '.format(message))
                
        item = {
            "id": {"S": str(uuid.uuid4())},
            "name": {"S": message['name']},
            "result": {"S": message['result']},
            "confidence": {"N": str(message['confidence'])},
            "timestamp": {"S": str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}
        }
        tableName = os.environ["dynamodbTableName"]
        
        dynamodb.put_item(TableName=tableName, Item=item)

    except Exception as e:
        print(e)
        raise e
    