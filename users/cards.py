from flask import Blueprint
from flask_restx import Api, Resource

from database.models import Card

bp = Blueprint('card', __name__)
api = Api(bp)

card_model = api.parser()
card_model.add_argument('user_id', type=int, required=True)
card_model.add_argument('card_number', type=int, required=True)
card_model.add_argument('card_name', type=str, required=True)
card_model.add_argument('exp_date', type=str, required=True)
card_model.add_argument('amount', type=float, required=True)

delete_card_model = api.parser()
delete_card_model.add_argument('card_number', type=int, required=True)


@api.route('/add-card')
class AddCard(Resource):
    @api.expect(card_model)
    def post(self):
        response = card_model.parse_args()
        user_id = response.get('user_id')
        card_number = response.get('card_number')
        card_name = response.get('card_name')
        exp_date = response.get('exp_date')
        amount = response.get('amount')

        try:
            Card().register_card(card_number, card_name, user_id, amount, exp_date)

            return {'status': 1, 'message': 'Карта успешно добавлена'}

        except Exception as e:
            return {'status': 0, 'message': str(e)}


@api.route('/delete-card')
class DeleteCard(Resource):
    @api.expect(delete_card_model)
    def delete(self):
        response = delete_card_model.parse_args()
        card_number = response.get('card_number')

        try:
            Card().delete_card(card_number)

            return {'status': 1, 'message': 'Карта успешно удалена'}

        except Exception as e:
            return {'status': 0, 'message': 'Ошибка в данных'}
