from flask_restplus import Namespace, fields


class UserModel:
    users_schema = Namespace('users', description='Users', validate=True)
    model = users_schema.model('users', {
        "nome": fields.String(required=True, description=(u'Descricao')),
        "email": fields.String(required=True, description=(u'Email')),
        "telefone": fields.String(required=True, description=(u'Telefone')),
        "pais": fields.String(required=False, description=(u'Pais')),
        "cidade": fields.String(required=False, description=(u'Cidade')),
        "endereco": fields.String(required=False, description=(u'Endereco')),
        "senha": fields.String(required=True, description=(u'Senha')),
        "verificado": fields.Boolean(required=True, description=(u'Verificado')),
    })

    # ● Nome (string: obrigatório)
    # ● Email (string: obrigatório)
    # ● Senha (string: Obrigatório, Hash)
    # ● Verificado (boolean: obrigatório)
    # ● Número de telefone(string: obrigatório)
    
    # ● País (string)
    # ● Cidade (string)
    # ● Endereço (string)
