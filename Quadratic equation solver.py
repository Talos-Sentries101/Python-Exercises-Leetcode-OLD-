import cmath
from numpy import around

def Quad(a, b, c):
    return_type_of_sqrt = cmath.sqrt((b ** 2) - (4 * a * c))
    root1 = (-b + return_type_of_sqrt) / (2 * a)
    root2 = (-b - return_type_of_sqrt) / (2 * a)
    print(around(root1, 2), around(root2, 2))


I = int(input('Enter the Value of a:'))
J = int(input('Enter the Value of b:'))
K = int(input("Enter the Value of c:"))

Quad(I, J, K)