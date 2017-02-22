def lis1(a,r):
    for i in a:
        for g in r:
            if i == g:
                return True
    return False

t = raw_input("ingrese palabra 1 ")
u = raw_input("ingrese palabra 2 ")
print lis1(t,u)