
def computepay(hours,valor):
    if hours<40:
        pago=hours*valor
    else:
        pago = 40*valor + (hours-40)*valor*1.5
    return print("Lo que ganarás es: " + str(pago))
try:
    trabajadas = float(input("Horas trabajadas: "))
    valorHora = float(input("Valor por hora: "))
    computepay(trabajadas,valorHora)
except:
    print("Los datos ingresados son incorrectos.")
