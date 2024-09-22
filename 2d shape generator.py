import turtle

para = ['yes', 'no', 'n', 'y']
colours = ['red', 'blue', 'yellow', 'purple', 'green', 'orange', 'black']
u_side = int(input('Enter the Number of sides for the polygon'))
u_angle = 360 // u_side
u_paracol = input('Do you want to the shape to have color?')
while True:
    u_paracol = input('Do you want to the shape to have color?')
    u_paracol.lower()
    if u_paracol in para:
        break
    else:
        print('Invalid input!! Enter yes or no (y or n)')
        continue
if u_paracol == 'yes' or 'y':
    print('The Available colours are:', colours)
    while True:
        u_col = input('Enter a colour')
        u_col.lower()
        if u_col not in colours:
            print('Invalid input!! Enter a valid colour from the list')
            continue
        else:
            break
screen = turtle.getscreen()
pen = turtle.Turtle()
pen.speed(1)
if u_paracol == 'yes' or 'y':
    pen.fillcolor(u_col)
    pen.begin_fill()
else:
    pen.fillcolor()
for line in range(u_side):
    pen.forward(100)
    pen.right(u_angle)
pen.end_fill()
