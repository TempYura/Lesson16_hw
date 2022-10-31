from models import User, Offer, Order


def init_database(db, raw_data):
    """Загружаем данные из raw файла"""

    db.drop_all()
    db.create_all()

    for user_data in raw_data.users:
        user = User(
            id=user_data.get("id"),
            first_name=user_data.get("first_name"),
            age=user_data.get("age"),
            email=user_data.get("email"),
            role=user_data.get("role"),
            phone=user_data.get("phone")
        )
        db.session.add(user)

    for order_data in raw_data.orders:
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

    for offer_data in raw_data.offers:
        offer = Offer(
            id=offer_data.get("id"),
            order_id=offer_data.get("order_id"),
            executor_id=offer_data.get("executor_id")
        )
        db.session.add(offer)

    db.session.commit()
