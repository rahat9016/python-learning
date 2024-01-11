
flag = True;

while flag:
    value = input("Enter your charter:-")
    if(value == 'A' or value == 'a'): 
        print(f"{value} is vowel");
    elif value == 'E' or value == 'e':
        print(f"{value} is vowel");
    elif value == 'I' or value == 'i':
        print(f"{value} is vowel");
    elif value == 'O' or value == 'o':
        print(f"{value} is vowel");
    elif value == 'U' or value == 'u':
        print(f"{value} is vowel");
    else:
        flag = False;
        print("Exit the program!")