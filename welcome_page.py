from log_in import log_in_to_account
from new_account import *

class Options:

    def welcome_page():
        print("****************************")
        print("WELCOME OUR BANK")
        print()

    def main_menu():

        while True:
            print("Select options:")
            options = ["1. Log-in to your account", "2. Create a new account", "3. Change your current password", "4. Exit"]
            for element in options:
                print(element)

            choice = input("Please select the option: ")

            if choice == "1":
                log_in_to_account()
            elif choice == '2':
                NewAccount.get_id_input()
                NewAccount.get_password_input()
                NewAccount.get_email_input()
                NewAccount.accept_regulation()
            elif choice == '3':
                print("Change password - feature coming soon!")
            elif choice == '4':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice, please enter a number between 1 and 4\n")