import json
from amqp import produce_message
from database import User


def default_callback(ch, method, properties, body):
    # TODO define router rules
    print('RECEIVE MESSAGE USER MICROSERVICE')
    payload = json.loads(body)
    print(" [x] Received %r" % payload)

    try:
        user_created = User.create(
            **payload
        )
        print('CREATED USER', user_created)
    except Exception as e:
        print(e)
        raise e

    produce_message('send_email', payload)