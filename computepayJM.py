def computepay(a):
    if a <= 40:
        c = a * 10
    else:
        c = a * 10.5
    return c

x =input("ingrese la cantidad de horas:")
try:
    x=float(x)
    computepay(x)
    print (computepay(x))
except:
    print ("no ingreso horas")
