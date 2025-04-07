import hashlib
from datetime import datetime
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

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def log_login_attempt(self, user_id, success):
        with open("login_attempts.log", "a", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status = "Success" if success else "Failure"
            log_file.write(f"{timestamp} - ID: {user_id} - Status: {status}\n")

    def save_to_file(self, user_id, password, email, regulation):
        hashed_password = self.hash_password(password)

        with open("dane.txt", "a", encoding="utf-8") as file:
            file.write(f"ID: {user_id}\n")
            file.write(f"Password: {hashed_password}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Accepted Regulation: {regulation}\n")
            file.write("-" * 30 + "\n")

    def open_file_login_checking(self,user_id, user_password):
        records_found = False
        temporary_user = {}

        with open('dane.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if line == "------------------------------":
                    if temporary_user.get("ID") == user_id:
                        if temporary_user.get("Password") == self.hash_password(user_password):
                            records_found = True
                            break
                        else:
                            break
                    else:
                        temporary_user = {}

                else:
                    if ":" in line:
                        key, value = line.split(":", 1)
                        temporary_user[key.strip()] = value.strip()

        return records_found