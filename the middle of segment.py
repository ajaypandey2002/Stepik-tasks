# объявление функции
def get_middle_point(x1, y1, x2, y2):
    m1 = float((x1 + x2)/2)
    m2 = float((y1 + y2)/2)
    return m1, m2

# считываем данные
x_1, y_1 = 0, 0
x_2, y_2 = 10, 0

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)