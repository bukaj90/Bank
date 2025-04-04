import re
class NewAccount:

    def __init__(self):
        print("CREATE A NEW ACCOUNT")
    @staticmethod
    def get_id_input(prompt):
        while True:
            correct_id = input(prompt)
            if correct_id.isdigit() and len(correct_id) == 8:
                return int(correct_id)
            else:
                print("Enter only digits and 8 characters")

    @staticmethod
    def get_password_input(prompt):

        while True:
            password = input(prompt)
            if re.fullmatch(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$",password):
                return password
            else:
                print("Error: Password must be at least 8 characters long, contain uppercase and lowercase letters, a number and a special character")


    @staticmethod
    def get_email_input(prompt):
        while True:
            email = input(prompt)
            if re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                return email
            else:
                print("Error: Please enter a valid email address")

    @staticmethod
    def accept_regulation(prompt):
        while True:
            regulation = input(prompt)
            if re.fullmatch(r"^yes$", regulation.lower()):
                print("Regulation has been accepted!!!")
                return regulation.lower()
            else:
                print("You must accept the regulation by typing YES.")
                print()

    def create_account(self):
        numer = self.get_id_input("Enter 8 digits ID: ")
        print("ID accepted!")
        print()

        correct_password = self.get_password_input("Enter your password 8 characters: ")
        reenter_password = self.get_password_input("Re-enter your password 8 characters: ")

        if correct_password != reenter_password:
            print("Error: Passwords do not match!")
        else:
            print("Password accepted!!")
            print()

        address_email = self.get_email_input("Enter your address email: ")
        reenter_email = self.get_email_input("Re-enter your email: ")

        if address_email != reenter_email:
            print("Error: Email do not match")
        else:
            print("Email accepted")
            print()

        accepted_regulation = self.accept_regulation("Please accept the regulation (yes): ")
