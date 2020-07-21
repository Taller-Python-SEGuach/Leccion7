def computepay(h,v):
    if h <= 40 :
       p = h*v

    if h > 40 :
       p = 40*v + (h-40)*1.5*v

    return print("A la semana ganará: " + str(p))

try:
    x = float(input("Ingrese horas de trabajo a la semana: "))
    y = float(input("Ingrese valor por hora trabajada: "))

    computepay(x,y)

except:
    print("Los datos son inválidos")
