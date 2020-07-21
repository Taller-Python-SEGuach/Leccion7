def computepay(h,p):
    if h<=40:
        pay=h*p
        return pay
    elif h>40:
        pay=40*p + (h-40)*p*1.5
        return pay

h=input("¿Cuantas horas trabajas?")
p=input("¿Cuanto te pagan por hora?")
try :
   h = float(h)
   p = float(p)
   computepay(h,p)
   print("Te pagarán", computepay(h,p))
except :
    print("Ingrese solo números")
