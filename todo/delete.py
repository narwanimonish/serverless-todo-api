import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')


def read(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    response = {
        "statusCode": 200
    }

    return response
