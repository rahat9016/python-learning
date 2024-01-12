password = 6;

program_running = True;
password_limit = 3;
count = 0

while program_running:
    count += 1
    user_pass = int(input("Enter you password:- "))
    if(user_pass == password):
        print("Signing successfully done!")
        break
    elif count > 3:
        print(f"Unauthorized user. you gave {count} time's password")
        break
    else:
        print("Password is wrong!")