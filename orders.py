PAST_ORDERS = "coffee_history.txt"

def order_coffee():
    print("\nChoose your favorite coffee:")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Mocha")

    option = input("Option: ")

    cafes = {
        "1": "Espresso",
        "2": "Latte",
        "3": "Cappuccino",
        "4": "Mocha"
    }

    if option in cafes:
        chosen_coffee = cafes[option]
        print("\nYour choise is: " + chosen_coffee + ". \nYour coffee is in preparation, please wait...")

        with open (PAST_ORDERS, "a", encoding="utf-8") as file:
            file.write(chosen_coffee + "\n")
    else:
        print("\nInvalid option, please try again.")

