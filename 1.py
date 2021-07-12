def func(a, b):
    return a / b

num1 = int(input('Введите делимое: '))
num2 = int(input('Введите делитель: '))
while num2 == 0:
    print('Делить на ноль нельзя!')
    num2 = int(input('Введите делитель: '))
print(func(num1, num2))