numbers = [5, 2, 4, 6, 1]

for item in numbers:
    print('*' * item)

for item in numbers:
    output= ''
    for count in range(item):
        output += 'x'
    print(output)