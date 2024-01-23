try:
    value = int(input("value:-"))
    age = int(input("age:-"))
    income = value / age
    print(income)
except ZeroDivisionError:
    print("Income can not be 0.")
except ValueError:
    print("Invalid value")