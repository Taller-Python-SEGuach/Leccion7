a =float(input("ingrese la cantidad de horas:"))
b =float(input("ingrese la paga por hora: "))
def computepay(a,b):
    if a <= 40:
        c = a * b
    else:
        c= ((a - 40)* b * 1.5) + 40 * b
    return c

print("Su paga es de:",computepay(a,b))
