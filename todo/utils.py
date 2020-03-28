import logging
import json


def validate_event_object(event):
    if 'body' not in event:
        logging.error('Data not present')
        raise Exection('Todo creation failed. Specify text')

    data = json.loads(event['body'])
    if 'task' not in data:
        logging.error('Text not present')
        raise Exection('Todo creation failed. Specify text')

    return data