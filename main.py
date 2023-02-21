from flask import Flask

from database.models import db
from flask_migrate import Migrate

from business import bp as business_bp
from users import bp as users_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/pay'
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(business_bp)
app.register_blueprint(users_bp)


@app.route('/')
def index():
    return 'Main page'
