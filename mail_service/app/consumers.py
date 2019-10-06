import json 


def default_callback(ch, method, properties, body):
    # TODO define routers and rules here!
    print('RECEIVE MESSAGE MAIL MICROSERVICE')
    payload = json.loads(body)
    print(" [x] Received %r" % payload)
    print('SEND EMAIL')
