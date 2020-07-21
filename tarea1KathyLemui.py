#Valor de mi hora hasta 40 horas trabajadas
# 10.5 = , a / horas = b / sueldo = c 
# Sobre 40 horas , el valor es 1.5 mas


#SUELDO SIN HORAS EXTRAS
def computepay (a,b):
    if a<=40 :
        c=a*b

#SUELDO CON HORAS EXTRAS
    else:
        c =40*b + ((a - 40)*1.5*b)
    return print ("Su sueldo sera de :" + str (c))

try:
    a = float(input("Numero de horas trabajadas a la semana:"))
    b = float(input("Valor de horas trabajadas:"))
    computepay(a,b)

except:
    print("Datos ingresados erroneos")
