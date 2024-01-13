price = [10, 20, 50, 5544]

total = 0
for item in price:
    total+=item
    print(f"Inner total is {total}")

print(f"Outer total is {total}")