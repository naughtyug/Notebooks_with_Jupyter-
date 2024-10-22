#single line comment

'''
multi line comment
'''

# declaring a variable
num = 'badd'
number_one = 35
number_two = 4.44
status = False

print(type(number_one))
print(number_one + number_two)

# returning function
def Subtraction():
    difference = number_one - number_two
    return difference

print(Subtraction())

#void Function
def Addition():
    sum = number_one + number_two
    print(sum)

Addition()
