import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')


def read(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        result = table.get_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
    except Exception as e:
        return {
            "statusCode": 404,
            "message": "Task not found."
        }

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
    }

    return response
