# import turtle

# screen = turtle.Screen()
# screen.bgcolor('orange')
# COLORS = ('red', 'green', 'blue', 'black')

# t = turtle.Pen()
# t.pensize(4)
# for c in range(12):
#     t.pencolor(COLORS[c % 4])
#     for i in range(4):
#         t.forward(100)
#         t.left(90)
#     t.left(30)


# screen.exitonclick()


# favorite_sports = ["football", "baseball", "basletball"]

favorite_sports = {
    'ali': 'football',
    'reza': 'baseball',
    'javad': 'tennis'

}

# print(favorite_sports['reza'])
favorite_sports['javad'] = 'skate'

print(favorite_sports)
