birth_year = input("Enter your birthday:")
# age = 2023 - birth_year;
print(type(birth_year))
year = int(birth_year)
print(type(year));
"""
    <class 'str'>
    <class 'int'>
"""

"""
# Error Message! 
Traceback (most recent call last):
  File "/home/minhajur/python-learning/first_module/data_type.py", line 2, in <module>
    age = 2023 -birth_year;
TypeError: unsupported operand type(s) for -: 'int' and 'str'
"""

