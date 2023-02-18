from datetime import datetime

from main import db


# Модель пользователя
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_phone_number = db.Column(db.String(11), unique=True, null=False)
    username = db.Column(db.String(75), null=False)
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
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    card_number = db.Column(db.Integer, unique=True, null=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), on_delete='SET NULL')
    card_amount = db.Column(db.Float)
    exp_date = db.Column(db.Date, null=False)
    added_date = db.Column(db.DateTime, default=datetime.now())

    # Регистрация карты
    def register_card(self, card_number, user_id, amount, exp_date):
        user_card = Card(card_number=card_number, amount=amount, user_id=user_id, exp_date=exp_date)
        db.session.add(user_card)
        db.session.commit()

    # Удалить карту
    def delete_card(self, card_number):
        current_card = Card.query.get_or_404(card_number)
        db.session.delete(current_card)
        db.session.commit()


# Модель платежей
class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id', on_delete='SET 0'), null=False)
    amount = db.Column(db.Float)
    pay_date = db.Column(db.DateTime, default=datetime.now())

    card = db.relationship('Card')

    # Создать платеж
    def create_payment(self, card_id, amount):
        payment = Payment(card_id=card_id, amount=amount)
        db.session.add(payment)
        db.session.commit()

# Модель бизнеса

# Модель сервиса

# Модель типа сервиса
