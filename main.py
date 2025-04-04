print("****************************")
print("WELCOME OUR BANK")
print()
print("Select options:")
print("1. Log-in to your account")
print("2. Create a new account")
print("3. Change your current password")
print()

#Option 1

print("To log-in, please provide your ID and password")
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
            print("Your account has been blocked due to multiple incorrect attemps")

