print('------\nЗадание "Программистам всё можно"\n------')

def add_everything_up(a,b):
    try:
        result = a + b
    except TypeError as exc:
        print('Сложение числа и строки:')
        result = str(a) + str(b)
        return result
    else:
        print('Стандартное сложение:')
        return result

print(add_everything_up(123.456, 'строка'), '\n')
print(add_everything_up('яблоко', 456), '\n')
print(add_everything_up(123.45, 7))

print('------')