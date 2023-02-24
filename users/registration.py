from flask import Blueprint
from flask_restx import Api, Resource

from database.models import User

# bp = Blueprint('registration', __name__)
# api = Api(bp)

from users import api

registration_model = api.parser()
registration_model.add_argument('username', type=str, required=True)
registration_model.add_argument('phone_number', type=str, required=True)

update_user_phone_number = api.parser()
update_user_phone_number.add_argument('user_id', type=int, required=True)
update_user_phone_number.add_argument('new_phone_number', type=str, required=True)


@api.route('/register')
class RegisterUser(Resource):
    @api.expect(registration_model)
    def post(self):
        response = registration_model.parse_args()
        username = response.get('username')
        phone_number = response.get('phone_number')

        try:
            user_id = User().register_user(phone_number, username)

            return {'status': 1, 'user_id': user_id}

        except Exception as e:
            return {'status': 0, 'message': str(e)}

    @api.expect(update_user_phone_number)
    def put(self):
        response = update_user_phone_number.parse_args()
        user_id = response.get('user_id')
        new_phone_number = response.get('new_phone_number')

        try:
            User().change_phone_number(user_id, new_phone_number)

            return {'status': 1, 'message': 'Номер успешно обновлен'}

        except Exception as e:
            return {'status': 0, 'message': 'Ошибка в данных'}
