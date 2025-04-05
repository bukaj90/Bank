import os
class WriteRead:

    def id_exist(self, user_id):
        if not os.path.exists("dane.txt"):
            return False

        with open("dane.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("ID: ") and user_id == line.strip().split("ID: ")[1]:
                    return True
        return False

    def email_exist(self, email):
        if not os.path.exists("dane.txt"):
            return False

        with open("dane.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("Email: ") and email == line.strip().split("Email: ")[1]:
                    return True
        return False

    def save_to_file(self, user_id, password, email, regulation):
        with open("dane.txt", "a", encoding="utf-8") as file:
            file.write(f"ID: {user_id}\n")
            file.write(f"Password: {password}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Accepted Regulation: {regulation}\n")
            file.write("-" * 30 + "\n")