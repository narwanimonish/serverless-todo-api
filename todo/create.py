import json
from datetime import datetime, timezone
import os
import uuid
import boto3
from todo.utils import validate_event_object


dynamodb = boto3.resource('dynamodb')


def create(event, context):

    data = validate_event_object(event)

    current_time = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'task': data['task'],
        'completed': False,
        'createdAt': current_time,
        'updatedAt': current_time,
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 201,
        "body": json.dumps(item)
    }

    return response
