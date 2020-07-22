def computepay (horas,valor):
    if horas<=40:
        pago=horas*valor
        return pago
    elif horas>40:
        pago=40*valor + (horas-40)*valor*1.5
        return pago

horas=input("¿cuantas horas trabajas en la semana?")
valor=input("¿cuanto te pagan por hora?")
try :
        horas = float(horas)
        valor = float(valor)
        computepay(horas,valor)
        print("te pagarán", computepay(horas,valor))
except :
        print("Ingrese solo números")
