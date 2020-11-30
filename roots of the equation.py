from math import *
def solve(a, b, c):
    D = b**2 - 4*a*c

    if D == 0:
        x1 = -b/(2*a)
        return x1, x1
    else:
        x1 = (-b + sqrt(D))/(2*a)
        x2 = (-b - sqrt(D))/(2*a)
        if x1 > x2:
            return x2, x1
        else:
        	return x1, x2

# считываем данные


# вызываем функцию
x1, x2 = solve(-2, 7, -5)
print(x1, x2)