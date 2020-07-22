def pago (a,b): #a=horas (h) y b=pago por hora (ph)
    c = a * b #c=total(t)
    return c

def Horas_extra (a,b,d):
    c=40*b + (a-40)*b*d
    return c

print("Aviso!!")
print("Su bonificación inicial será de 1.0!)")
print("(Despues de 40 horas de trabajo, su bonificación aumenta a 1.5!)")
print("Veamos cuando dinero ganara usted =")

horas=input ("Ingrese las horas de trabajo :")
pago_hora=input ("Ingrese el pago por hora :")
horas_extras=input ("ingrese su bonificación de horas extras:")

h=float(horas)
ph = float(pago_hora)
hx=float(horas_extras)

pago(h,ph)
Horas_extra (h,ph,hx)

if h <= 40:
    print("Usted ganará", pago (h,ph) , "a la semana.")

elif h > 40:
    print ("Usted ganará", Horas_extra(h,ph,hx), "a la semana.")
