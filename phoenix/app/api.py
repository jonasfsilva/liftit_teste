from flask import Flask
from flask_restplus import Api, Resource
from models import UserModel


app = Flask(__name__)
api = Api(app=app)


api_usuarios = UserModel.users_schema
api.add_namespace(api_usuarios)


@api_usuarios.route("/")
class UserList(Resource):
    
    @api_usuarios.expect(UserModel.model, validate=True)
    def post(self):
        return {}, 201

    def get(self):
        return [], 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')