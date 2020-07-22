def computepay(horas,pagoprom):
  if horas <=40 :
    sueldo = horas*pagoprom
  if horas >40 :
    sueldo = pagoprom*40 + (horas-40)*1.5*pagoprom
  return print("El sueldo que recibes asciende a:" + str(sueldo))

try:
  x = float(input("Ingrese el número de horas trabajadas semanalmente: "))
  y = float(input('Ingrese el pago promedio por hora trabajada: '))

  computepay(x,y)

except:
  print("Ingrese las horas como números enteros")
