from amqp import open_conn
from amqp import start_consumers
from consumers import default_callback


def run_consumers():
    connection = open_conn()
    queue = 'create'
    start_consumers(connection, default_callback, queue)


def main():
    run_consumers()
    # TODO consumir o que veio da API
    # TODO produzir para o envio de email
    # pass


if __name__ == "__main__":
    main()