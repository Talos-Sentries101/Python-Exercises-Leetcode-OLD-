import math


def triangle():
    if u_val == 'area':
        b = float(input(' length of base'))
        h = float(input('Height'))
        final = 1 / 2 * float(h) * float(b)
        print('The Area of the Triangle is', final)
    elif u_val == 'height':
        b = float(input('length of base'))
        a = float(input('area of the triangle'))
        final = (2 * b) / a
        print('The Height of the Triangle is', final)
    elif u_val == 'base' or ' length of base':
        a = float(input('area of the triangle'))
        h = float(input('Height'))
        final = (2 * h) / a
        print('The Length of the base is:', final)


def circle():
    if u_para == 'area' and u_val == 'area':
        r = float(input('Enter the radius'))
        final = math.pi * (float(r) ** 2)
        print('The area of the circle is:', final)
    elif u_para == 'area' and u_val == 'radius' or 'r':
        a = float(input('Area of circle'))
        final = math.sqrt(a // math.pi)
        print('The radius of the sphere is:', final)
    elif u_para == 'circumference' or 'perimeter' and u_val == 'circumference' or 'perimeter':
        r = float(input('Enter the radius'))
        final = math.tau * r
        print('The circumference of the circle is:', final)
    elif u_para == 'circumference' or 'perimeter' and u_val == 'radius' or 'r':
        c = float(input('perimeter of circle'))
        final = c // math.tau
        print('The radius of the sphere is:', final)


def square():
    if u_para == 'area' and u_val == 'area':
        s = float(input('Enter the length of the side'))
        final = math.pow(s, 2)
        print('The area of the square is:', final)
    elif u_para == 'area' and u_val == 'side' or 'length of side':
        a = float(input('Area of the square'))
        final = math.sqrt(a)
        print('The side of the square is of length', final)
    elif u_para == 'circumference' or 'perimeter' and u_val == 'circumference' or 'perimeter':
        s = float(input('Enter the length of the side'))
        final = 4 * s
        print('The perimeter of the square is:', final)
    elif u_para == 'circumference' or 'perimeter' and u_val == ' side' or 'length of side':
        a = float(input('Area of the square'))
        final = a // 4
        print('The side of the square is of length', final)


def rectangle():
    if u_para == 'area' and u_val == 'area':
        l = float(input('Length'))
        b = float(input('Breadth'))
        final = l * b
        print('The area of the Rectangle is:', final)
    elif u_para == 'area' and u_val == 'length':
        b = float(input('Breadth'))
        a = float(input('Enter the area of the rectangle'))
        final = a // b
        print('The length of the Rectangle is:', final)
    elif u_para == 'area' and u_val == 'Breadth':
        l = float(input('Length'))
        a = float(input('Enter the area of the rectangle'))
        final = a // l
        print('The Breadth of the Rectangle is:', final)
    elif u_para == 'circumference' or 'perimeter' and u_val == 'circumference' or 'perimeter':
        b = float(input('Breadth'))
        l = float(input('length'))
        final = 2 * (l + b)
        print(final)
    elif u_para == 'circumference' or 'perimeter' and u_val == 'length':
        b = float(input('Breadth'))
        p = float(input('The perimeter of the rectangle'))
        final = p - (2 * b) // 2
        print('The length of the Rectangle is:', final)
    elif u_para == 'circumference' or 'perimeter' and u_val == 'Breadth':
        l = float(input('length'))
        p = float(input('The perimeter of the rectangle'))
        final = p - (2 * l) // 2
        print('The Breadth of the Rectangle is:', final)


def sphere():
    if u_para == 'volume' and u_val == 'volume':
        r = float(input('Enter the radius of the sphere'))
        final = 4 // 3 * math.pi * (math.pow(r, 3))
        print('The Volume of sphere is:', final)
    elif u_para == 'volume' and u_val == 'radius' or 'radius of sphere':
        v = float(input('The volume of the sphere'))
        final = ((3 * v) // (4 * math.pi)) ** 1 / 3
        print('Radius of Sphere is:', final)
    elif u_para == 'total surface area' or 'tsa' or 'csa' or 'curved surface area' and u_val == 'total surface area' or 'tsa' or 'csa' or 'curved surface area':
        r = float(input('Enter the radius of the sphere'))
        final = 4 * math.pi * (r ** 2)
        print('The Surface area of the sphere is:', final)
    elif u_para == 'total surface area' or 'tsa' or 'csa' or 'curved surface area' and u_val == 'radius' or 'radius ' \
                                                                                                            'of sphere':
        s = float(input("Enter the surface area of the sphere"))
        final = math.sqrt((s // (4 * math.pi)))
        print('Radius of Sphere is:', final)


def cylinder():
    if u_para == 'volume' and u_val == 'volume':
        r = float(input('Enter the radius of the cylinder'))
        h = float(input('Height'))
        final = math.pi * h * (r ** 2)
        print('The Volume of the Cylinder is', final)
    elif u_para == 'volume' and u_val == 'radius' or 'radius of the cylinder' or 'radius of cylinder':
        h = float(input('Height'))
        v = float(input('Enter the Volume of the cylinder'))
        final = math.sqrt(v // (h * math.pi))
        print(final)
    elif u_para == 'volume' and u_val == 'height' or 'height of cylinder':
        r = float(input('Enter the radius of the cylinder'))
        v = float(input('Enter the Volume of the cylinder'))
        final = v // (r ** 2) * math.pi
        print('The Height of the cylinder is', final)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'total surface area' or 'tsa':
        r = float(input("Enter the radius of the cylinder"))
        h = float(input('Height'))
        final = math.tau * r * (r + h)
        print('The total surface area of the cylinder is', final)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'radius' or 'radius of the cylinder' or 'radius of cylinder':
        h = float(input('Height'))
        ts = float(input('Enter the Total surface are of the Cylinder'))
        final = math.sqrt(ts // (math.tau * h))
        print(('The radius of the cylinder is:', final))
    elif u_para == 'total surface area' or 'tsa' and u_val == 'height' or 'height of cylinder':
        h = float(input('Enter the height of the cylinder'))
        ts = float(input('Enter the Total surface are of the Cylinder'))
        final = math.sqrt((((h ** 2) + 2 * ts // math.pi) - h) / 2)
        print('The height of the cylinder is:', final)
    elif u_para == "csa" or 'curved surface area' and u_val == "csa" or 'curved surface area':
        r = float(input('Enter the radius of the cylinder'))
        h = float(input('Height'))
        final = math.tau * r * h
        print(final)
    elif u_para == "csa" or 'curved surface area' and u_val == 'radius' or 'radius of the cylinder' or 'radius of cylinder':
        h = float(input('Height'))
        cs = float(input('Enter the lateral surface area of the Cylinder'))
        final = cs // (math.tau * h)
        print(('The radius of the cylinder is:', final))
    elif u_para == "csa" or 'curved surface area' and u_val == 'height' or 'height of cylinder':
        r = float(input('Enter the radius of the cylinder'))
        cs = float(input('Enter the lateral surface area of the Cylinder'))
        final = cs // (math.tau * r)
        print('The height of the cylinder is:', final)


def cube():
    if u_para == 'volume' and u_val == 'volume':
        s = float(input('Enter the length of the side'))
        final = math.pow(s, 3)
        print('The Volume of the cube is:', final)
    elif u_para == 'volume' and u_val == 'side' or 'side of the cube':
        v = float(input('Enter the Volume of the cube'))
        final = v ** 1 / 3
        print('The Side of the cube is of length:', final)
    elif u_para == 'csa' or 'curved surface area' and u_val == 'csa' or 'curved surface area':
        s = float(input('Enter the length of the side'))
        final = 4 * math.pow(s, 2)
        print(final)
    elif u_para == 'csa' or 'curved surface area' and u_val == 'side' or 'side of the cube':
        cs = float(input('Enter the Lateral surface area of the cube'))
        final = math.sqrt(cs // 4)
        print('The Side of the cube is of length:', final)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'total surface area' or 'tsa':
        s = float(input('Enter the length of the side'))
        final = 6 * (math.pow(s, 2))
        print(final)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'side' or 'side of the cube':
        ts = float(input('Enter the Total surface area of the cube'))
        final = math.sqrt(ts // 6)
        print('The Side of the cube is of length:', final)


def cone():
    if u_para == 'volume' and u_val == 'volume':
        r = float(input('Enter the radius of the cone'))
        h = float(input('Height'))
        final = 1 / 3 * math.pi * (r ** 2) * h
        print('The Volume of the cone is:', final)
    elif u_para == 'volume' and u_val == 'radius' or ' radius of cone':
        h = float(input('Height'))
        v = float(input('Enter the Volume of the cone:'))
        final = math.sqrt((3 * v) // (math.pi * h))
        print('The radius of the cone is:', final)
    elif u_para == 'volume' and u_val == 'height' or 'height of cone':
        r = float(input('Enter the radius of the cone'))
        v = float(input('Enter the Volume of the cone:'))
        final = 3 * v // (r ** 2) * h
        print('The Height of the cone is:', final)
    elif u_para == 'csa' or 'curved surface area' and u_val == 'csa' or 'curved surface area':
        u_l_height = input('Do you have the value of the Slant Height?')
        if u_l_height != True:
            r = float(input('Enter the radius of the cone'))
            h = float(input('Height'))
            l = math.sqrt((r ** 2) + (h ** 2))
            final = math.pi * r * l
            print(final)
        else:
            r = float(input('Enter the radius of the cone'))
            l = float(input('Enter the Slant Height:'))
            final = math.pi * r * l
            print(final)
    elif u_para == 'csa' or 'curved surface area' and u_val == 'radius' or 'radius of cone':
        u_l_height = input('Do you have the value of the Slant Height?')
        if u_l_height != True:
            u_height = input('Do you have the Height of the cone?')
            if u_height == True:
                h = float(input('Height'))
                final = math.sqrt(l ** 2 - h ** 2)
                print('The Radius of the cone is', final)
            else:
                print('Can not compute radius for given parameter under given conditions!!')
        else:
            print('Can not compute radius for given parameter under given conditions!!')
    elif u_para == 'total surface area' or 'tsa' and u_val == 'total surface area' or 'tsa':
        u_l_height = input('Do you have the value of the Slant Height?')
        if u_l_height != True:
            r = float(input('Enter the radius of the cone'))
            h = float(input('Height'))
            l = math.sqrt((r ** 2) + (h ** 2))
            final = math.pi * r * (l + r)
            print(final)
        else:
            r = float(input('Enter the radius of the cone'))
            l = float(input('Enter the Slant Height:'))
            final = math.pi * r * (l + r)
            print(final)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'radius' or 'radius of cone':
        u_l_height = input('Do you have the value of the Slant Height?')
        if u_l_height != True:
            u_height = input('Do you have the Height of the cone?')
            if u_height == True:
                h = float(input('Height'))
                final = math.sqrt(l ** 2 - h ** 2)
                print('The Radius of the cone is', final)
            else:
                print('Can not compute radius for given parameter under given conditions!!')
        else:
            print('Can not compute radius for given parameter under given conditions!!')


def cuboid():
    if u_para == 'volume' and u_val == 'volume':
        l = float(input('Length'))
        b = float(input('Breadth'))
        h = float(input('Height'))
        final = l * b * h
        print('The Volume of the Cuboid is', final)
    elif u_para == 'volume' and u_val == 'length':
        v = float(input('Enter the Volume of the cube'))
        b = float(input('Breadth'))
        h = float(input('Height'))
        final = v // (b * h)
        print('The Length of the cuboid is:', final)
    elif u_para == 'volume' and u_val == 'breadth':
        v = float(input('Enter the Volume of the cube'))
        l = float(input('Length'))
        h = float(input('Height'))
        final = v // l * h
        print('The Breadth of the cuboid is:', final)
    elif u_para == 'volume' and u_val == 'height':
        v = float(input('Enter the Volume of the cube'))
        l = float(input('Length'))
        b = float(input('Breadth'))
        final = v // l * b
        print('The Height of the cuboid is:', final)
    elif u_para == 'csa' or 'curved surface area' and u_val == 'csa' or 'curved surface area':
        l = float(input('Length'))
        b = float(input('Breadth'))
        h = float(input('Height'))
        final = 2 * h * (l + b)
        print('The lateral surface area of the cylinder is:', final)
    elif u_para == 'csa' or 'curved surface area' and u_val == 'length':
        cs = float(input('Enter the lateral surface area or CSA:'))
        b = float(input('Breadth'))
        h = float(input('Height'))
        final = cs - (h * b) // (2 * h)
        print('The Length of the cuboid is:', final)
    elif u_para == 'csa' or 'curved surface area' and u_val == 'breadth':
        cs = float(input('Enter the lateral surface area or CSA:'))
        l = float(input('Length'))
        h = float(input('Height'))
        final = cs - (2 * h * l) // (2 * h)
        print('The Breadth of the cuboid is:', final)
    elif u_para == 'csa' or 'curved surface area' and u_val == 'height':
        cs = float(input('Enter the lateral surface area or CSA:'))
        l = float(input('Length'))
        b = float(input('Breadth'))
        final = cs // 4 * l * b
        print('The Height of the cuboid is:', final)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'total surface area' or 'tsa':
        l = float(input('Length'))
        b = float(input('Breadth'))
        h = float(input('Height'))
        final = 2 * ((l * h) + (b * h) + (l * b))
        print(final)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'length':
        ts = float(input('Enter the Total surface area:'))
        b = float(input('Breadth'))
        h = float(input('Height'))
        final = ts - (2 * b * h) // (4 * b * h)
        print('The Length of the cuboid is:', final)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'breadth':
        ts = float(input('Enter the Total surface area:'))
        h = float(input('Height'))
        l = float(input('Length'))
        final = ts - (2 * l * h) // (4 * l * h)
    elif u_para == 'total surface area' or 'tsa' and u_val == 'height':
        ts = float(input('Enter the Total surface area:'))
        l = float(input('Length'))
        b = float(input('Breadth'))
        final = ts - (2 * l * b) // (4 * l * b)


# list of all shapes both 2d and 3d in separate lists
print('Welcome to the calculator!!!')
d2_shapes = ['triangle', 'circle', 'square', 'rectangle', ]
d3_shapes = ['sphere', 'cylinder', 'cube', 'cuboid', 'cone']
shapes = [d2_shapes + d3_shapes]
diemensions = ['2d', '3d']
# The assessment criterion for the said shapes as per their dimension
d2_para = ['area', 'circumference', 'perimeter']
d3_para = ['Total surface area', 'volume', 'curved surface area', 'csa', 'tsa']
A_para = d2_para + d3_para
circle_val = ['radius','area','circumference' or 'perimeter']
triangle_val = ['']

while True:
    u_id = input("Which dimension of shapes 2d shape or 3d shape:")
    u_id = u_id.lstrip()
    u_id = u_id.lower()
    if u_id in diemensions:
        break
    else:
        print('Invalid Input!! Please select between 2d or 3d shapes')
if u_id == '2d':
    print('The 2d shapes available ae:', d2_shapes)
elif u_id == '3d':
    print('The 3d shapes available are:', d3_shapes)
while True:
    u_shape = input("Choose your shape:")
    u_shape = u_shape.lower()
    u_shape = u_shape.lstrip()
    if u_id == '2d' and u_shape in d2_shapes:
        break
    elif u_id == '3d' and u_shape in d3_shapes:
        break
    else:
        print('Invalid input!!! Please select from the list of shapes')
if u_id == '2d':
    print('The operations for 2d figures are:', d2_para)
elif u_id == '3d':
    print('The operations for 3d figures are:', d3_para)
while True:
    u_para = input("Which parameter would you like to assess:")
    u_para = u_para.lower()
    u_para = u_para.lstrip()
    if u_id == '2d' and u_para in d2_para:
        break
    elif u_id == '3d' and u_para in d3_para:
        break
    else:
        print('Invalid input!! Please select one of the given parameters')
u_val = input("Enter the missing parameter:")
u_val = u_val.lower()
u_val = u_val.lstrip()
if u_shape == 'triangle':
    triangle()
elif u_shape == 'circle':
    circle()
elif u_shape == 'square':
    square()
elif u_shape == 'rectangle':
    rectangle()
elif u_shape == 'sphere':
    sphere()
elif u_shape == 'cylinder':
    cylinder()
elif u_shape == 'cube':
    cube()
elif u_shape == 'cuboid':
    cuboid()
elif u_shape == 'cone':
    cone()
