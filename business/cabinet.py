from flask import Blueprint
from flask_restx import Api, Resource

from database.models import ServiceType

# bp = Blueprint('cabinet', __name__)
# api = Api(bp)

from business import api

model_service_register = api.parser()
model_service_register.add_argument('service_name', type=str, required=True)
model_service_register.add_argument('service_type', type=str, required=True)


@api.route('/add-service')
class AddService(Resource):
    @api.expect(model_service_register)
    def post(self):
        response = model_service_register.parse_args()
        service_name = response.get('service_name')
        service_type = response.get('service_type')

        try:
            ServiceType().register_service(service_name, service_type)

            return {'status': 1, 'message': 'Сервис успешно добавлен'}

        except Exception as e:
            return {'status': 0, 'message': str(e)}

