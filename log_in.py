def log_in_to_account():
    print("To log-in, please provide your ID and password")

    # Data with file
    correct_id = '123'
    correct_password = '123'

    max_attempts = 4
    attempts_left = max_attempts

    while attempts_left > 0:
        user_id = str(input("Enter your ID: "))
        user_password = str(input("Enter your password: "))
        print()

        if user_id == correct_id and user_password == correct_password:
            print("Login successfully")
            break
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Incorrect login or password. You have {attempts_left} attempts left.")
                print()
            else:
                print("Your account has been BLOCKED due to multiple incorrect attempts")
                print()