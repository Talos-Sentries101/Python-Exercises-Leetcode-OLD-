import turtle

lst_user_shape = ['cube', 'cuboid']
lst_speed = ['fast', 'slow','medium' ]
print(lst_user_shape)
while True:
    user_shape = input('Enter the Shape to be drawn')
    if user_shape in lst_user_shape:
        break
    else:
        print('Invalid input!!')
        continue
print(lst_speed)
while True:
    speed = input('Enter the Speed of Pen')
    speed.lower()
    if speed in lst_speed:
        break
    else:
        print('Invalid input!!')
        continue
if speed == 'slow':
    speed = 1
elif speed == 'fast':
    speed = 3
elif speed == 'medium':
    speed = 2
screen = turtle.getscreen()
p = turtle.Turtle()
turtle.title("3d Shape Generator ")
p.speed(speed)


def draw_square():
    for line in range(4):
        p.forward(200)
        p.right(90)


def draw_cuboid():
    for line in range(4):
        p.forward(200)
        p.right(90)
    p.goto(-200, 200)
    for lines in range(4):
        p.forward(200)
        p.right(90)
    p.right(90)
    p.forward(200)
    p.goto(0, -200)
    p.left(90)
    p.forward(200)
    p.left(135)
    p.forward(290)
    p.penup()
    p.right(46)
    p.forward(195)
    p.pendown()
    p.right(134)
    p.forward(285)


def draw_cube():
    draw_square()
    p.goto(-100, 100)
    draw_square()
    p.penup()
    p.right(90)
    p.forward(200)
    p.pendown()
    p.goto(0, -200)
    p.penup()
    p.goto(100, -100)
    p.pendown()
    p.right(180)
    p.forward(200)
    p.goto(200, 0)
    p.goto(200, -200)
    p.goto(94, -94)


if user_shape == 'cube':
    draw_cube()
elif user_shape == 'cuboid':
    draw_cuboid()
