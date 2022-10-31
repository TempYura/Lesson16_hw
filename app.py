import json

from flask import jsonify, request
from config import db, app
from models import User, Order, Offer
from utils import init_database

import raw_data


@app.route("/users", methods=["GET", "POST"])
def users_page():
    if request.method == "GET":
        users = [user.to_dict() for user in User.query.all()]
        db.session.close()
        return jsonify(users)

    if request.method == "POST":
        user_data = json.loads(request.data)
        user = User(
            id=user_data.get("id"),
            first_name=user_data.get("first_name"),
            email=user_data.get("email"),
            role=user_data.get("role"),
            phone=user_data.get("phone")
        )
        db.session.add(user)
        db.session.commit()

        return ""


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def users_uid_page(uid):
    if request.method == "GET":
        user = User.query.get(uid).to_dict()
        return json.dumps(user)

    if request.method == "PUT":
        user_data = json.loads(request.data)
        user = User.query.get(uid)
        user.first_name = user_data["first_name"]
        user.last_name = user_data["last_name"]
        user.age = user_data["age"]
        user.email = user_data["email"]
        user.role = user_data["role"]
        user.phone = user_data["phone"]

        db.session.add(user)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        user = User.query.get(uid)

        db.session.delete(user)
        db.session.commit()

        return ""


@app.route("/orders", methods=["GET", "POST"])
def orders_page():
    if request.method == "GET":
        orders = [order.to_dict() for order in Order.query.all()]
        db.session.close()
        return jsonify(orders)

    if request.method == "POST":
        order_data = json.loads(request.data)
        order = Order(
            id=order_data.get("id"),
            name=order_data.get("name"),
            description=order_data.get("description"),
            start_date=order_data.get("start_date"),
            end_date=order_data.get("end_date"),
            address=order_data.get("address"),
            price=order_data.get("price"),
            customer_id=order_data.get("customer_id"),
            executor_id=order_data.get("executor_id")
        )
        db.session.add(order)
        db.session.commit()

        return "", 201


@app.route("/orders/<int:oid>", methods=["GET", "PUT", "DELETE"])
def orders_uid_page(oid):
    if request.method == "GET":
        order = Order.query.get(oid).to_dict()
        return jsonify(order)

    if request.method == "PUT":
        order_data = json.loads(request.data)
        order = Order.query.get(oid)

        order.id = order_data.get("id")
        order.name = order_data.get("name")
        order.description = order_data.get("description")
        order.start_date = order_data.get("start_date")
        order.end_date = order_data.get("end_date")
        order.address = order_data.get("address")
        order.price = order_data.get("price")
        order.customer_id = order_data.get("customer_id")
        order.executor_id = order_data.get("executor_id")

        db.session.add(order)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        order = Order.query.get(oid)

        db.session.delete(order)
        db.session.commit()

        return ""


@app.route("/offers", methods=["GET", "POST"])
def offers_page():
    if request.method == "GET":
        offers = [offer.to_dict() for offer in Offer.query.all()]
        db.session.close()
        return jsonify(offers)

    if request.method == "POST":
        offer_data = json.loads(request.data)
        offer = Offer(
            id=offer_data.get("id"),
            order_id=offer_data.get("order_id"),
            executor_id=offer_data.get("executor_id")
        )
        db.session.add(offer)
        db.session.commit()

        return "", 201


@app.route("/offers/<int:oid>", methods=["GET", "PUT", "DELETE"])
def offers_uid_page(oid):
    if request.method == "GET":
        offer = Offer.query.get(oid).to_dict()
        return jsonify(offer)

    if request.method == "PUT":
        offer_data = json.loads(request.data)
        offer = Offer.query.get(oid)

        offer.id = offer_data.get("id")
        offer.order_id = offer_data.get("order_id")
        offer.executor_id = offer_data.get("executor_id")

        db.session.add(offer)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        offer = Offer.query.get(oid)

        db.session.delete(offer)
        db.session.commit()

        return ""


if __name__ == "__main__":
    init_database(db, raw_data)
    app.run()
