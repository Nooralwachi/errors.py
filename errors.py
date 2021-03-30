# Exceptions and Errors

#TypeError: cannot concatenate 'str' and 'int' objects
print('The lucky number is' +2)

#ValueError: invalid literal for int() with base 10: 'Hello World'
num= int('Hello World')

#ZeroDivisionError: integer division or modulo by zero
print(5/0)

#IOError: [Errno 2] No such file or directory: 'wrongname.txt'
file = open('wrongname.txt','r')

#AttributeError: 'int' object has no attribute 'append'
x= 10
x.append(5)

#NameError: name 'prit' is not defined
prit('hello')


