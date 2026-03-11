def validate_email(email):
    return "@" in email and "." in email


def validate_price(price):
    return price > 0