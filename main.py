from services.user_service import create_user
from services.order_service import create_order

def main():
    user = create_user("Mandeep", "mandeep@email.com")

    order = create_order(
        user_id=user["id"],
        product="Laptop",
        price=90000
    )

    print("User Created:", user)
    print("Order Created:", order)

if __name__ == "__main__":
    main()
