

def create_new_entry():
    with open("dane.txt", "a", encoding="utf-8") as plik:
        plik.write(f"ID: {numer}\n")
        plik.write(f"Password: {correct_password}\n")
        plik.write(f"Email: {address_email}\n")
        plik.write(f"Accepted Regulation: {accepted_regulation}\n")
        plik.write("-" * 30 + "\n")

    print("Account has been saved to dane.txt!")


def get_id_input(self, prompt):
    while True:
        correct_id = input(prompt)
        if correct_id.isdigit() and len(correct_id) == 8:
            return int(correct_id)
        else:
            print("Enter only digits and 8 characters")

        if self.id_exist(correct_id):
            print("This ID already exists! Please enter a different one.")
            continue
        return correct_id