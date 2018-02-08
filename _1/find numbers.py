# internal and external types of data

import sys

_message = sys.argv[0]

# _ = internal to program.  protected. python best practice

#strings
_str = "this is a str"
_str_2 = 'this is a str'
#in python, ' and " are treated the same
_str = f'{_str_2} test'
#interpolation string
#if python 2, must use .format(_str_2=str_2)

#boolean
_bool = True
_bool_false = False
#anything 0 = true, anything not 0 = false

#integers = whole number. can be negative
_int = 1
_int_negative = -1

#Floats = decimals
_float = 1.0
_float_negative = -1.0

#casting
output = int('1') + 1
output2 = '1' + str(1)

print(output)
print(output2)

print(bool(0))
print(bool(1))
print(bool(.1))
print('---')

print(len(''))
print(len('false'))

#list
_list = ['alex', 'grande', 'sara',
         'danie', 'laura', 'jen']
_list2 = list()

for name in _list:
    print(name)



# message = 'hello world'
#
# print(message)

"""
practice: print each letter in a given string
"""

message = "programming 101"

#brute for method - manual
print('p')
print('r')
print('o')
print('g')
print('r')
print('a')
print('m')
print('m')
print('i')
print('n')
print('g')
print(' ')
print('1')
print('0')
print('1')

print('----')

#for <variable_name> in <collection>:
#       <action>
#for is an iterator

for letter in message:
    print(letter)



"""
practice: print true or false if a letter exists in a given string
"""

#logical
search_value = 'a'
message = 'hello world'

if search_value in message:
    print(True)
else:
    print(False)

"""
practice: elif statements
"""

# message = 'hello world'
#
# if message = 'hello world'
#     print('1')
# elif == 'danielle'
#     print('2')
# else
#     print('3')

"""
practice: print each letter in a given string
"""

name = 'name'
for character in name:
    print(character)

"""
practice: create a function that takes an input, 
then prints each character of the input
"""

def print_character(input):
    for character in input:
        print(character)
print_character('wonder woman')

#search is a variable
#== compares
#= assigns
def search_character(search, find):
    is_found = False
    for character in find:
        if character == search:
            is_found = True

            print(True)
search_character('a', 'purple')

#comparisons
# == equals
# != not equal
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# = is the assignment of

"""
practice: create a function that tkes an input, 
then prints each character of the input
"""

def print_characters(input_string: str):
    #print('\n'.join(input_string))
    for character in input_string:
        print(character)

"""
Practice: create a function that takes two inputs,
then prints True/False whether or not the first input
is contained within the second input
"""

text_value = 'some input'
def search_string(search, text_input):
    result=False
    for character in text_input:
        if character == search:
            result=True
    print(result)

search_string('a', text_value) #False
search_string('s', text_value) #True
search_string('S', text_value) #False