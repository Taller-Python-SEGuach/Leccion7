def computepay(horas,valor):
    if horas<=40:
        sueldo=horas*valor
#horas de horario laboral
    else:
        sueldo=40*valor + ((horas-40)*valor*1.5)
    return print("Tu sueldo será de: " + str(sueldo))
#horas de horario laboral más horas extra
try:
    hrtrabajadas = float(input("Ingrese el numero de horas que trabajo: "))
    valorxhora = float(input("Ingrese el valor por hora de trabajo: "))
    computepay(hrtrabajadas,valorxhora)
except:
    print("Error en el ingreso de sus datos")
