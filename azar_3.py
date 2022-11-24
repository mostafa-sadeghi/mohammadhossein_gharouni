# strings = []

# for i in range(5):
#     string = input(f'Enter string {i+1}/5 > ')
#     strings.append(string)

# print('________________________________________')

# for i in range(4, -1, -1):
#     print(f'String number {i+1}/5: {strings[i]}')

# example 2

# max([100, ‘blue’, 3.5, ‘sugar on the rocks’, 7.0]) > 7.0
# max([7, 2, 9, 1])  > None

def max_(l):
    max_float = []
    for item in l:
        if type(item) == float:
            max_float.append(item)
    if len(max_float) == 0:
        return None
    # return max(max_float)
    max_float.sort()
    return max_float[-1]


print(max_([100, 'blue', 3.5, 'sugar on the rocks', 7.0]))
print(max_([7, 2, 9, 1]))


# exercise1 : do it without max_float list بدون استفاده از لیست تمرین بالا رو انجام بده
# exercise 2: write a function that get a list of strings and return biggest/largets string from that list
