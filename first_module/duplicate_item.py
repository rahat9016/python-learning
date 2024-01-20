numbers = [1,12,4,2,21,3,4,1,43,32,12,3]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)