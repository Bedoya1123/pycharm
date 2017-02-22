def cuadros(n):
    sum = 0
    if n<= 100:
        for i in range(1,n):
            if i % 4==0:
                t = i**2
                sum = sum + t
    print sum

t = input(" Ingrese un numero ")
cuadros(t)


