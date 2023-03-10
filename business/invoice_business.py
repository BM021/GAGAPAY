from flask import Blueprint
from flask_restx import Api, Resource

from database.models import Payment, User, Card

# bp = Blueprint('invoice', __name__)
# api = Api(bp)


from business import api

invoice_model = api.parser()
invoice_model.add_argument('service_id', type=int, required=True)
invoice_model.add_argument('service_name', type=str, required=True)
invoice_model.add_argument('amount', type=float, required=True)
invoice_model.add_argument('phone_number', type=str, required=True)


@api.route('/send-invoice')
class SendInvoice(Resource):
    @api.expect(invoice_model)
    def post(self):
        response = invoice_model.parse_args()
        service_id = response.get('service_id')
        service_name = response.get('service_name')
        amount = response.get('amount')
        phone_number = response.get('phone_number')

        user_id = User.query.filter_by(user_phone_number=phone_number).first().id
        card_number = Card.query.filter_bY(user_id=user_id).first().card_number

        payment = Payment().create_payment(card_number, amount, service_name)

        if payment:
            return {'status': 1, 'message': 'Успешно отправлено'}

        return {'status': 0, 'message': 'Не достатично денег'}
