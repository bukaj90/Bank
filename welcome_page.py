from log_in import log_in_to_account
from new_account import NewAccount

class Options:
    @staticmethod
    def welcome_page():
        print("****************************")
        print("WELCOME IN OUR BANK")
        print()


        while True:
            print("Select options:")
            options = ["1. Log-in to your account", "2. Create a new account", "3. Change your current password", "4. Exit"]
            for element in options:
                print(element)
            try:
                choice = input("Please select the option: ")

                if choice == "1":
                    log_in_to_account()
                elif choice == '2':
                    account = NewAccount()
                    account.create_account()
                elif choice == '3':
                    print("Change password - feature coming soon!")
                elif choice == '4':
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid choice, please enter a number between 1 and 4\n")
            except KeyboardInterrupt:
                print("\nProgram interrupted. Exiting...")
                break