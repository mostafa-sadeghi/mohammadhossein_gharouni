def is_sym(number):
    # number = str(number)
    return number == number[::-1]


number = input('enter number >')
if is_sym(number):
    print(f'{number} is symmetric')
else:
    print(f'{number} is not symmetric')

#  Todo define function to reverse number instead of using slice
#  Todo create menu
