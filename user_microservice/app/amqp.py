import pika


BROKER_URL = 'amqp://admin:12345678@rabbitmq_rb/'


def open_conn():
    parameters = pika.URLParameters(BROKER_URL)
    connection = pika.BlockingConnection(parameters)
    return connection


def declare_queue(connection, queue):
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    return channel


def produce_message(message, connection):
    channel = declare_queue(connection)
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

    print(" [x] Sent 'Hello World!'")
    connection.close()


# def default_callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)


def start_consumers(connection, callback_func, queue):
    channel = declare_queue(connection, queue)
    channel.basic_consume(
        queue=queue, on_message_callback=callback_func, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
