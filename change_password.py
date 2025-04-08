from write_read import WriteRead
import re

def reset_password():
    print("Changing an existing passwor")

    user_id = input(str("Enter your ID: "))
    address_email = input("Enter email assigned to account: ")

    password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$"

    update = False
    new_line = []

    with open("dane.txt", "r") as file:
        for line in file:
            part = line.strip().split(",")
            if len(part) == 3:
                ID, password, email = part

                if ID == user_id and emial == address_email:
                    new_password = input("Enter your new password (8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char): ")

                    if re.match(password_pattern, new_password):
                        new_line.append(f"{user_id}, {address_email}, {new_password}\n")
                        update = True
                else:
                    new_line.append(line)
            else:
                new_line.append(line)
    if update:
        with open("dane.txt", "w") as file:
            file.writelines(new_line)
            print("Password changed successfully")
    else:
        print("Incorrect login or email")