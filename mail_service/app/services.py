import logging


logging.basicConfig(filename="teste.log", level=logging.INFO)


def make_link_to_ativate_user(payload):
    return "http://link_to_ativate_user"


def send_message_to_confirmation_user(payload):
    print('ENVIANDO EMAIL')
    nome = payload.get('nome')
    email = payload.get('email')
    link = make_link_to_ativate_user(payload)
    logging.info('SEND EMAIL')
    logging.info("Nome: {0} | Email: {1} | Link: {2}".format(nome, email, link))

    