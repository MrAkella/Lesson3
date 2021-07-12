def my_sum():
    res = 0
    while True:
        line = input('Введите числа, разделенные пробелами или В для выхода: ').split()
        for num in line:
            if num == 'd' or num == 'в':
                return res
            else:
                res = res + int(num)
        print('Сумма чисел = ', res)

print('Итоговая сумма = ', my_sum())