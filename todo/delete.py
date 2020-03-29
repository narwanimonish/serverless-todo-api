import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        result = table.delete_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
    except Exception as e:
        return {
            "statusCode": 404,
            "message": "Task not found"
        }

    response = {
        "statusCode": 200,
        "message": "Deleted task successfully."
    }

    return response
