from menu import show_menu
from orders import order_coffee
from history import view_order_history

def main():
    while True:
        show_menu()
        option = input("Enter an option: ")

        if option == "1":
            order_coffee()
        elif option == "2":
            view_order_history()
        elif option == "3":
            print("\nExiting the Coffee Shop. Goodbye!")
            break
        else:
            print("\nInvalid option, please try again:")

if __name__ == "__main__":
    main()