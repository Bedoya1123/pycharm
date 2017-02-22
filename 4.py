def voc (f):
    if f == "a" or f == "e" or f == "i" or f == "o" or f == "u":
        return True
    elif f == "A" or f == "E" or f == "I" or f == "O" or f == "U":
        return True
    else :
        return False

c=raw_input("ingrese una letra: ")
print voc(c)
