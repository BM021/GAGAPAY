from flask import Blueprint
from flask_restx import Api, Resource

bp = Blueprint('registration', __name__)
api = Api(bp)

registration_model = api.parser()
registration_model.add_argument('username', type=str, required=True)
registration_model.add_argument('phone_number', type=str, required=True)


@api.route('/register')
class RegisterUser(Resource):
    @api.expect(registration_model)
    def post(self):
        pass
