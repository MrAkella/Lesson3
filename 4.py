# 1 "ежи"
# def my_func(x, y):
#    return (x)**(y)
#
# num1 = int(input('Введите число: '))
# num2 = int(input('Введите степень: '))
# print (my_func(num1, num2))

# 2 цикл
def my_func(x, y):
    i = 0
    res = 1
    while i < abs(y):
        res = res * x
        i += 1
    if y < 0:
        res = 1 / res
    return res

print(my_func(2, -1))
