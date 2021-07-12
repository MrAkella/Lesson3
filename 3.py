def my_func(x, y, z, ):
    list = [x, y, z]
    list.remove(min(x, y, z))
    return sum (list)

print (my_func(9, 2, 3))