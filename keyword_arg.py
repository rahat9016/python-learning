def greet_user(first_name, last_name):
    print(f"your full name is {first_name} {last_name}")

greet_user(first_name="Minhajur", last_name="Rohoman")

# wrong way we are declared
#greet_user(first_name="Minhajur", "Rohoman") # we will get an error  > Positional argument cannot appear after keyword arguments
# correct way is like that
greet_user("Minhajur", last_name="Rohoman")
