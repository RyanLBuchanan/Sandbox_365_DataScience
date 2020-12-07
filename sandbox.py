# Intro tutorial to Python Progammer Bootcamp | Giles McMullen-Klein | input by Ryan Buchanan 21NOV20


# print('Hello world!')

# x = 5

# y = 12

# z = x + y 

# print(z)

# new_variable = 13

# z = x - y

# a, b, c = 2.5, 3.14159, 1

# c = b * a**2

# radius = 2.5

# pi = 3.14159

# area = pi * radius**2

# phrase_1 = 'The cat sat on the mat!'

# phrase_2 = 'And so did the dog!'

# phrase_3 = phrase_1 + ' ' + phrase_2

# print(phrase_3)

# user_input = int(input('How many apples do you have?\n>>> '))

# type(user_input)

# help()

# while = 5

# def area_circ():
    
#     pi = 3.14159
    
#     radius = float(input('What\'s the radius of your circle, please?\n>>> '))
    
#     area = pi * radius**2
    
#     return print('You entered:', radius, '\nThe area of your circle is approximately:', area, 'units.')

# area_circ()
    
''' Convert Fahrenheit to Celsius '''

# def conv_F2C():
    
#     Fahrenheit_input = float(input("What's the Fahrenheit temperature, please?\n>>>"))
    
#     Celsius_output = (Fahrenheit_input - 30) / 2
    
#     print("You enetered:", Fahrenheit_input, '\n', Fahrenheit_input, 'degrees in Fahrenheit is', Celsius_output, 
#           'degrees in Celsius.')

# conv_F2C()    

# def conv_F2C_exact():
    
#     Fahrenheit_input = float(input("What's the Fahrenheit temperature, please?\n>>> "))
    
#     Celsius_output = round(((Fahrenheit_input - 32) * 5/9), 2)
    
#     print("You entered:", Fahrenheit_input, '\nSo then,', Fahrenheit_input, 'degrees in Fahrenheit is', Celsius_output, 
#           'degrees in Celsius.')

# conv_F2C_exact()    

# def sum_num():
#
#     num_1 = int(input('Please enter the first number: '))
#
#     num_2 = int(input('Please enter the second number: '))
#
#     sum_tot = num_1 + num_2
#
#     print('The sum of ' + str(num_1) + ' + ' + str(num_2), ' = ' + str(sum_tot) + '\nThanks for playing, my Good Man!')
#
# sum_num()

# x = 5
# y = 6
#
# print('x = ', x, 'y = ', y)
# print('Checking less than with \'<\':', x < y)
# print('Checking greater than with \'>\':', x > y)

# var_1 = 7
# var_2 = 7
#
# print('var_1 = ', var_1, 'var_2 = ', var_2)
# print('Check equality with \'==\':', var_1 == var_2)
# print('Check not equal with \'!=\':', var_1 != var_2)
# print('Check less than or equal with \'<=\':', var_1 <= var_2)
# print('Check greater than or equal with \'>=\':', var_1 >= var_2)
#
# var_3, var_4, var_5 = 15, 20, 25
#
# print(var_3, var_4, var_5)
#
# print(not(var_3 <100 and var_5 < 100))
#
# print(not(var_3 < 22 and var_5 < 22))
#
# print(not(var_3 < 22 or var_5 < 22))

# some_condition = True
#
# if some_condition:
#     print('The variable \'some_condition\' is True')
# else:
#     print('The variable \'some_condition\' is False')
#

# temp = int(input('Please enter the temoerature in Celsius. \nAn integer between 0-40:  '))
#
# if temp > 30:
#     print('Wear your dainty Brit short pants.')
# elif temp <= 30 and temp > 20:
#     print('Keep a fleece with ya just in case.')
# elif temp <= 20 and temp > 10:
#     print('Better bring a jacket, then.')
# else:
#     print('Right, then . . . let\'s just stay in, shall we?')

my_string = 'Python'

letter = my_string[3]