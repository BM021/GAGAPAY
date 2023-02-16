from flask import Blueprint
from flask_restx import Api, Resource

bp = Blueprint('card', __name__)
api = Api(bp)

card_model = api.parser()
card_model.add_argument('card_number', type=int, required=True)
card_model.add_argument('exp_date', type=str, required=True)
card_model.add_argument('card_name', type=str, required=True)
card_model.add_argument('phone_number', type=str, required=True)

delete_card_model = api.parser()
delete_card_model.add_argument('card_number', type=int, required=True)
delete_card_model.add_argument('user_id', type=int, required=True)


@api.route('/add-card')
class AddCard(Resource):
    @api.expect(card_model)
    def post(self):
        pass


@api.route('/delete-card')
class DeleteCard(Resource):
    @api.expect(delete_card_model)
    def delete(self):
        pass
