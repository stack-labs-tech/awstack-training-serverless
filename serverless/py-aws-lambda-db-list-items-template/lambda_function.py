import boto3
import json
import uuid
import datetime
import decimal

import ast
import os

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):

    try:
        tableName = os.environ["dynamodbTableName"]
        print('List items from table {} '.format(tableName))
        table = dynamodb.Table(tableName)

        result = table.scan()
                
        print('{} items found !'.format(result['Count']))
        
        print(result['Items'])
        return {
           "headers":{
              "Access-Control-Allow-Origin":"*"
           },
           "body": json.dumps(result['Items'], cls=ComplexEncoder)
       }

    except Exception as e:
        print(e)
        raise e
    

class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, decimal.Decimal):
            return float(z)
        else:
            super().default(self, z)
