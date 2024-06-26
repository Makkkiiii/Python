username = "jhilke"
password = "jhilke@1"
attempt_c = 0

while attempt_c < 3:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    
    if input_username == username and input_password == password:
        print("Login successful!")
        break
    else:
        print("Incorrect username or password.")
        attempt_c += 1

if attempt_c == 3:
    print("Sorry! You entered wrong username or password for third time, you cannot login.")