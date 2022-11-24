# print('''
# to exit press > 0,
# to add number enter 1 and to show th result enter show
# to show sum > 2
# ''')
# numbers = []
# while True:
#     entry = input("enter your choice> ")
#     if entry == '0':
#         exit()
#     elif entry == '1':
#         while True:
#             number = input("enter number or enter 'show' to showing result> ")
#             if number == "show":
#                 print(f'sum of {len(numbers)} numbers is : {sum(numbers)}')
#                 exit()
#             else:
#                 numbers.append(int(number))

#     elif entry == '2':
#         print(f'sum of {len(numbers)} numbers is : {sum(numbers)}')
#         exit()


# name = input("enter your name:> ")
# family = input("enter your name:> ")

# print(f'Hello {name} {family}')


# numbers = []

# numbers.append('ali')
# numbers.append(2)
# numbers[0] = 7
# print(numbers)


# import random

# frequency_1 = 0
# frequency_2 = 0
# frequency_3 = 0
# frequency_4 = 0
# frequency_5 = 0
# frequency_6 = 0


# for roll in range(6_000_000):
#     face = random.randrange(1, 7)
#     if face == 1:
#         frequency_1 += 1
#     elif face == 2:
#         frequency_2 += 1
#     elif face == 3:
#         frequency_3 += 1
#     elif face == 4:
#         frequency_4 += 1
#     elif face == 5:
#         frequency_5 += 1
#     elif face == 6:
#         frequency_6 += 1

# print(f'Face{"Frequencies":>15}')
# print(f'{1:>4}{frequency_1:>15}')
# print(f'{2:>4}{frequency_2:>15}')
# print(f'{3:>4}{frequency_3:>15}')
# print(f'{4:>4}{frequency_4:>15}')
# print(f'{5:>4}{frequency_5:>15}')
# print(f'{6:>4}{frequency_6:>15}')


import random


def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return(die1, die2)


def display_dice(dice):
    die1, die2 = dice  # (3,5)
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')


die_values = roll_dice()
display_dice(die_values)


sum_of_dices = sum(die_values)
# if sum_of_dices == 7 or sum_of_dices == 11:
if sum_of_dices in (7, 11):
    game_status = "WON"
elif sum_of_dices in (2, 3, 12):
    game_status = "LOST"
else:
    game_status = 'CONTINUE'
    my_point = sum_of_dices
    print('my point is : ', my_point)

while game_status == 'CONTINUE':
    print('press enter to continue!!!')
    input("> ")
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dices = sum(die_values)
    if sum_of_dices == my_point:
        game_status = "WON"
    elif sum_of_dices == 7:
        game_status = "LOST"


if game_status == "WON":
    print("you are the winner!!!")
else:
    print("you lose!!!!!")
