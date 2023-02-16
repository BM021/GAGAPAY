from flask import Blueprint
from flask_restx import Api, Resource

bp = Blueprint('monitoring', __name__)
api = Api(bp)


monitoring_model = api.parser()
monitoring_model.add_argument('card_number_or_all', type=str, required=True)


@api.route('/expenses')
class Monitoring(Resource):
    @api.expect(monitoring_model)
    def get(self):
        pass
