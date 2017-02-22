def contar_digitos(n):
        ind = 0
        while n > 0:
            q= n % 10
            n = n / 10
            ind = ind + q
        if ind % 2 == 0:
            print (" Es un numero par y tiene "+ str(ind)+ " digitos ")
        else:
            print (" Es un numero impar y tiene "+ str(ind)+ " digitos ")

a = input(" Ingrese el valor ")
contar_digitos(a)