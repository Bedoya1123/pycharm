def cantidad_digitos(n):
    ind = 1
    while n >9:
        n = n/10
        ind = ind +1
    print ind
cantidad_digitos(100000)
