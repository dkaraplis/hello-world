# internal and external types

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

#int = whole number. can be negative
_int = 1
_int_negative = -1
_float = 1.0

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

search_value = 'a'
message = 'hello world'

if search_value in message:
    print(True)
else:
    print(False)

