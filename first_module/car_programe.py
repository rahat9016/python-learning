start_car = True
stated = False
while start_car:
    command = input("Enter your command:\n1. Help\n2. Exit: ").lower()
    if command == 'help' or command == '1':
        car_start = input("Is car start [Yes/No]: ").lower()
        if car_start == 'yes':
            if stated:
                print("Car Already stated...")
            else:
                stated = True
                print("Yes car is star...")
        else:
            if not stated:
                print("Car Already stopped...")
            else:
                stated = False
                print("No car isn't start!")
    elif command == 'exit' or command == '2':
        print("Exit the programme...")
        break
    else:
        print("I don't understand!")
