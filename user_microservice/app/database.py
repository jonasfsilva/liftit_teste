from peewee import *


db = SqliteDatabase('teste.db')


class User(Model):
    
    class Meta:
        database = db
        db_table = 'user'

    nome = CharField()
    email = CharField()
    telefone = CharField()
    pais = CharField()
    cidade = CharField()
    endereco = CharField()
    senha = CharField()
    verificado = BooleanField()


User.create_table()
