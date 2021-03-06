import json
import logging
from datetime import datetime, timezone
import os
import boto3
from todo.utils import validate_event_object


dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = validate_event_object(event)

    current_time = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        result = table.update_item(
            Key={
                'id': event['pathParameters']['id']
            },
            ExpressionAttributeNames={
                '#todo_task': 'task',
            },
            ExpressionAttributeValues={
                ':task': data['task'],
                ':completed': bool(data['completed']) if 'completed' in data else False,
                ':updatedAt': current_time,
            },
            UpdateExpression='SET #todo_task = :task, '
                             'completed = :completed, '
                             'updatedAt = :updatedAt',
            ReturnValues='ALL_NEW',
        )
    except Exception as e:
        return  {
            "statusCode": 500,
            "message": "Updating task failed."
        }

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'])
    }

    return response
