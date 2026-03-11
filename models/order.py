class Order:

    def __init__(self, id, user_id, product, price):
        self.id = id
        self.user_id = user_id
        self.product = product
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product": self.product,
            "price": self.price
        }