import re
from write_read import WriteRead
class NewAccount:

    def __init__(self):
        print("CREATE A NEW ACCOUNT")
        self.write = WriteRead()

    def get_id_input(self, prompt):
        while True:
            correct_id = input(prompt)
            if not correct_id.isdigit() or len(correct_id) != 8:
                print("Enter only digits and 8 characters")
                continue

            if self.write.id_exist(correct_id):
                print("This ID already exists! Please enter a different one.")
                continue
            return correct_id

    def get_password_input(self,prompt):

        while True:
            password = input(prompt)
            if re.fullmatch(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$",password):
                return password
            else:
                print("Error: Password must be at least 8 characters long, contain uppercase and lowercase letters, a number and a special character")



    def get_email_input(self, prompt):
        while True:
            email = input(prompt)
            if not re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                print("Error: Please enter a valid email address")
                continue

            if self.write.email_exist(email):
                print("This email is already used. Please enter another.")
                continue
            return email

    def accept_regulation(self, prompt):
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
        print("ID accepted!\n")
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

        self.write.save_to_file(numer, correct_password, address_email,accepted_regulation)

        print("Your account has been created. You can log in now")