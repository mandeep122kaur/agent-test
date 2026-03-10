from models.user import User
from utils.validator import validate_email
from database.db_connection import insert
from utils.logger import log


def create_user(name, email):

    if not validate_email(email):
        raise ValueError("Invalid email")

    user = User(
        id=1,
        name=name,
        email=email
    )

    log("Creating user")

    return insert("users", user.to_dict())
