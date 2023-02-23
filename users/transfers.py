from flask import Blueprint
from flask_restx import Api, Resource

from database.models import TransfersP2P

bp = Blueprint('transfers', __name__)
api = Api(bp)

transfer_model = api.parser()
transfer_model.add_argument('user_from_id', type=int, required=True)
transfer_model.add_argument('user_from_card', type=int, required=True)
transfer_model.add_argument('to_card', type=int, required=True)
transfer_model.add_argument('amount', type=float, required=True)


@api.route('/transfer-money')
class Transfers(Resource):
    @api.expect(transfer_model)
    def post(self):
        args = transfer_model.parse_args()
        user_from_id = args.get('user_form_id')
        user_from_card = args.get('user_form_card')
        to_card = args.get('to_card')
        amount = args.get('amount')

        result = TransfersP2P().create_payment(user_from_id, user_from_card, to_card, amount)

        return {'status': 1, 'message': result}
