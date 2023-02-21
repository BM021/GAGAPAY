from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()


# Модель пользователя
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_phone_number = db.Column(db.String(11), unique=True, nullable=False)
    username = db.Column(db.String(75), nullable=False)
    reg_date = db.Column(db.DateTime, default=datetime.now())

    # Регистрация пользовотеля
    def register_user(self, phone_number, username):
        user = User(phone_number=phone_number, username=username)
        db.session.add(user)
        db.session.commit()

    # Изменить номер телефона
    def change_phone_number(self, user_id, new_phone_number):
        current_phone_number = User.query.get_or_404(user_id)
        if current_phone_number.user_phone_number == new_phone_number:
            return 'Новый телефон номер не должен совподать со старым'

        current_phone_number.user_phone_number = new_phone_number
        db.session.commit()


# Модель карт
class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer, unique=True, autoincrement=True)
    card_number = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))
    card_amount = db.Column(db.Float)
    exp_date = db.Column(db.Date, nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.now())

    # Регистрация карты
    def register_card(self, card_number, user_id, amount, exp_date):
        user_card = Card(card_number=card_number, amount=amount, user_id=user_id, exp_date=exp_date)
        db.session.add(user_card)
        db.session.commit()

    # Получение карты
    def get_card_object(self, card_id):
        current_card = Card.query.get_or_404(card_id)
        return current_card

    # Удалить карту
    def delete_card(self, card_id):
        current_card = Card.query.get_or_404(card_id)
        if current_card:
            db.session.delete(current_card)
            db.session.commit()

            return True

        return False


# Модель платежей
class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id', ondelete='SET NULL'), nullable=False)
    amount = db.Column(db.Float)
    pay_date = db.Column(db.DateTime, default=datetime.now())

    card = db.relationship('Card')

    # Создать платеж
    def create_payment(self, card_id, amount):
        card = Card().get_card_object(card_id=card_id)
        if card.amount >= amount:
            new_pay = Payment(card_id=card_id, card=card, amount=amount)
            db.session.add(new_pay)
            db.session.commit()

            return True

        return False


# Модель бизнеса
class Business(db.Model):
    __tablename__ = 'businesses'
    id = db.Column(db.Integer, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), primary_key=True)
    service_name = db.Column(db.String(60))
    business_card = db.Column(db.Integer, db.ForeignKey('cards.card_number'))
    service_type = db.Column(db.String, db.ForeignKey('services.service_type_name'))
    opened = db.Column(db.DateTime, default=datetime.now())

    card_date = db.relationship(Card)

    # Регистрация бизнесса
    def register_business(self, user_id, service_name, service_type, which_card):
        checker = Card.query.get_or_404(which_card)

        if checker and checker.user_id == user_id:
            new_business = Business(user_id=user_id, service_name=service_name,
                                    business_card=which_card, card_date=checker, service_type=service_type)

            db.session.add(new_business)
            db.session.commit()

            return True

        return False


# Модель типа сервиса
class ServiceType(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    service_category = db.Column(db.String)
    service_type_name = db.Column(db.String, unique=True)
    opened = db.Column(db.DateTime, default=datetime.now())

    # Регистрация типа сервиса
    def register_service(self, service_name, service_type_name):
        new_service_type = ServiceType(service_name=service_name, service_type_name=service_type_name)
        db.session.add(new_service_type)
        db.session.commit()

        return True
