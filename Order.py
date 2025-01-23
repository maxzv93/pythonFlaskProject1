class Order:
    def __init__(self, id, desc, items):
        self.id = id
        self.description = desc
        self.items = items

    def __repr__(self):
        return f'<Order {self.id}: {self.items} - {self.description}>'

orders = {43: Order(43, 'Оплата картой, через почту', ['Кружка', 'Майка', 'Стикеры']), 69: Order(69, 'Оплата наличными, через почту', ['Медные диски'])}

# from flask import Flask, request
# app = Flask(__name__)
#
#
# @app.route("/", methods=["POST"])
# def render_send():
#     client_message = request.form.get('id')
#     return orders[client_message]
