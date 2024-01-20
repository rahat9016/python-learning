numbers = [1, 45, 556, 54]

numbers.append(10) # append item in the numbers an array at the last
# print(numbers)

length_of_numbers = len(numbers)
mid = int(length_of_numbers / 2) # divided length of numbers

numbers.insert(mid, 45) #insert item in the middle of numbers an array
print(numbers)

numbers.pop() # The pop function will remove last item of numbers an array
print(numbers)

print(numbers.index(1))
print( 50 in numbers)
print(numbers.count(1))

numbers.sort()
print("sort",numbers)
numbers.sort(reverse=True)
print("reverse",numbers)
numbers.reverse()
print(numbers)

numbers_2 = numbers.copy()
print(numbers_2)
numbers.clear() # clear numbers array by clear function 
print(numbers)