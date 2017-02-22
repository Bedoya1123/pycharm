def solicitar(n):
    ind = 1
    while n >=10:
        n = n/10
        ind = ind +1
        if ind % 2 ==0:
            print ind

q= input(" Ingrese un numero ")
solicitar(q)