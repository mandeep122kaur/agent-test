from models.order import Order
from utils.validator import validate_price
from database.db_connection import insert
from utils.logger import log


def create_order(user_id, product, price):

    if not validate_price(price):
        raise ValueError("Invalid price")

    order = Order(
        id=1,
        user_id=user_id,
        product=product,
        price=price
    )

    log("Creating order")

    return insert("orders", order.to_dict())