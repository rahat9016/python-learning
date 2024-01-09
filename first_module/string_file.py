course = "Python course";

# print first index (output[P])
print(course[0]);
# print last index (output[e])
print(course[-1]);

# print first to third char (output[pyt])
print(course[0:3]);

# print index 0 char to last (output[Python course])
print(course[0:]);
# another way print string (output[Python]);
print(course[:6])

another = course[:];
print(another)

# print 1 to -1

print(course[1:-1]);

# formate string
special_course = "You have taken a "
formate_string = f'{special_course} [{another}]'
print(formate_string)

