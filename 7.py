def inv (c):
    d = ""
    x = len(c)
    s = -1
    while x >= 1:
        d=d+c[s]
        s= s-1
        x = x-1
    return d

def pali (c):
    pol= inv(c)
    s =0
    p =0
    for i in range (len(c)):
        if pol[s]== c[s]:
            s=s+1
            p=p+1
        else :
            print ("no es palimdrome")
            break
    if p==len(c):
        print ("palindromo")

a = raw_input("ingrese una palabra ")

print inv(a)
print pali(a)