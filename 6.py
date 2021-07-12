def int_func(line):
    return line.capitalize()
line = input('Введите слово: ')
print(int_func(line))

string = input('Введите строку: ').split()
res = []
for el in string:
    res.append(int_func(el))
print(' '.join(res))


