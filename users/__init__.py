from flask import Blueprint

from . import cards, monitoring, registration, service_payments, transfers

bp = Blueprint('user-pay', __name__, url_prefix='/user')

bp.register_blueprint(cards.bp)
bp.register_blueprint(monitoring.bp)
bp.register_blueprint(registration.bp)
bp.register_blueprint(service_payments.bp)
bp.register_blueprint(transfers.bp)
