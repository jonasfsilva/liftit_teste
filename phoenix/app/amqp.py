import pika
import json


BROKER_URL = 'amqp://admin:12345678@rabbitmq_rb/'


def open_conn():
    parameters = pika.URLParameters(BROKER_URL)
    connection = pika.BlockingConnection(parameters)
    return connection


def declare_queue(connection, queue):
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    return channel


def produce_message(queued, message):
    connection = open_conn()
    channel = connection.channel()
    channel.exchange_declare(exchange='users', exchange_type='topic')

    try:
        channel.basic_publish(exchange='users', routing_key=queued, body=json.dumps(message))
    except Exception as e:
        print(e)
        raise e

    print(" [x] Sent %r" % message)
    connection.close()


def start_consumers(connection, callback_func, queue):
    channel = declare_queue(connection, queue)
    channel.basic_consume(
        queue=queue, on_message_callback=callback_func, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
