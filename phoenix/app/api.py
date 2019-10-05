import json
from flask import Flask
from flask_restplus import Api, Resource
from flask import request
from models import UserModel
from amqp import open_conn
from amqp import produce_message


app = Flask(__name__)
api = Api(app=app)


api_usuarios = UserModel.users_schema
api.add_namespace(api_usuarios)


@api_usuarios.route("/")
class UserList(Resource):
    
    @api_usuarios.expect(UserModel.model, validate=True)
    def post(self):
        produce_message("create", json.loads(request.data))
        return {}, 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')