def palabra(n):
    q = raw_input(" Ingrese una palabra ")
    for i in n:
        if len(n)>len(q):
            q=n
    return q
t = raw_input(" Ingrese una palabra ")
print palabra(t)
