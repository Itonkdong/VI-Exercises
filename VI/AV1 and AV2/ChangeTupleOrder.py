def change_order(lista):
    return [(value, key) for (key, value) in lista]


print(change_order([(1, 'a'), (2, 'b'), (3, 'c')]))
