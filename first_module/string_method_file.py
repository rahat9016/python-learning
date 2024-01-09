# python building function
#len() it will return number, like down the print string has 11 char
print(len("Hello world"));

course = "Python is the best for course for us!"
new_course = course.upper() # the upper function does course string small char to upper case
print(new_course)
lower_new_course = new_course.lower();
print(lower_new_course);

# find char from string
print(course.find('P')) # 0
print(course.find('p')) # -1
print(course.find('c')) # 23

# replace function
title = "hello world"
print(title.replace('world', 'world!'))

# boolean expiration in string
print('hello' in title)
print(title.title())

title.upper()
title.lower()
title.find('p')
title.title()
title.replace()
'express' in title