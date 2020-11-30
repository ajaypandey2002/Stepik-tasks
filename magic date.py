# объявление функции
def is_magic(date):
    date = [int(x) for x in date.split('.')]
    if date[0] * date[1] == date[2]%100:
        return True
    else:
        return False

# считываем данные
date = '10.06.1960'

# вызываем функцию
print(is_magic(date))