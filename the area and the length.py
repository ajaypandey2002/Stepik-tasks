from math import *
def get_circle(radius):
    c = 2 * pi * radius
    s = pi * radius**2
    return c, s

# считываем данные
r = 1.5

# вызываем функцию
length, square = get_circle(r)
print(length, square)
