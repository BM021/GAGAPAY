from flask import Blueprint
from flask_restx import Api, Resource

bp = Blueprint('service_payments', __name__)
api = Api(bp)


service_payment_model = api.parser()
service_payment_model.add_argument('service_id', type=int, required=True)
service_payment_model.add_argument('amount', type=float, required=True)


@api.route('pay-service')
class ServicePayment(Resource):
    @api.expect(service_payment_model)
    def post(self):
        pass
