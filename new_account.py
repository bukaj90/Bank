#1. Login
#2. hasło
#3. powtorz haslo
#4. zaznaczenie regulaminu yes, no - w przypadku braku zgody wymagać zaznaczenia
#5. wysłanie danych do pliku ID, passowrd, email  - stworzyć plik kodujący i rozkodowywujacy, jak wpisane kilka razy złe hasło to w pliku wprowadzic ****
#6. zabezpieczenie przed wprowadzeniem za długich za krótkich nazw id i hasla, sprawdzanie poprawnosci email składnia

print("CREATE A NEW ACCOUNT")

correct_id = input("Enter 3 digit ID: ")

correct_password = input("Enter 3 digit password: ")
repeat_correct_password = input("Repeat password: ")

address_email = input("Enter your address email: ")
repeat_address_email = input("Repeat your address email: ")

accept_regulation = input("Please acceptance ot the Regulation (yes/no): ")

exit = input("Enter Exit to terminate the process")


if correct_password != repeat_correct_password:
    print("Incorrect password, enter again")
else:
    print("Your account has been created, you can log in")

if address_email != address_email:
    print("Incorrect address email or repeat address")


if accept_regulation.lower() != 'yes':
    print("You must accept the regulations to proceed.")
else:
    print("Regulations accepted. Welcome!!")