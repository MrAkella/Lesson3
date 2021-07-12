def case(**kwargs):
    return ', '.join(kwargs.values())


name = input('Введите имя: ')
lastname = input('Введите фамилию: ')
age = input('Введите возраст: ')
city = input('Введите город: ')
email = input('Введите e-mail: ')

print(case(name = name, lastname = lastname, age = age, city = city, email = email))
