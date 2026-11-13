PAST_ORDERS = "coffee_history.txt"

def view_order_history():
    try:
        print("\n Your past coffee orders:")
        with open(PAST_ORDERS, "r", encoding="utf-8") as file:
            orders = file.readlines()
            if orders:
                for i, order in enumerate(orders, start=1):
                    print(str(i) + ". " + order.strip())
            else:
                print("\nThere are no past orders yet. But we can change that now! ")
    except FileNotFoundError:
        print("\nThere are no past orders yet. But we can change that now! ")
