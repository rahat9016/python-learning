customer = {
    "name": "Minhajur Rohoman",
    "age": 23,
    "phone": "+8801638627290",
    "is_verified": True,
    "is_active": False,
    "has_computer": True,
    "has_mobile": True
}

# Get customer name value
print(customer["name"])
# Get customer name using get function
print(customer.get("name"))
# Key Error - because small charter and big charter is not name in python
#print(customer["Name"]) # if you want to get name value of customer use name not Name

print(customer)
# dictionary key value modification
customer["name"] = "Rahat"
print(customer)