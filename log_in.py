from write_read import WriteRead
def log_in_to_account():
    print("To log-in, please provide your ID and password")

    wr = WriteRead()
    max_attempts = 4
    attempts_left = max_attempts

    while attempts_left > 0:
        user_id = str(input("Enter your ID: "))
        user_password = str(input("Enter your password: "))
        print()

        print("Checking your login details...\n")
        record_found = wr.open_file_login_checking(user_id, user_password)


        if record_found:
            print("Login successfully")
            wr.log_login_attempt(user_id, success=True)
            break

        else:
            if wr.id_exist(user_id):
                attempts_left -= 1
                print(f"ID or password is incorrect. You have {attempts_left} attempts left.\n")

            else:
                print("ID or password is incorrect.\n")

            wr.log_login_attempt(user_id, success=False)

            if attempts_left == 0:
                print("Your account has been BLOCKED due to multiple incorrect attempts\n")
                break
