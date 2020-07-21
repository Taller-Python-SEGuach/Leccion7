


def computer_pay(horas,valor):
    if horas<=40:
        pago=horas*valor
    else:
        pago=(40*valor)+((horas-40)*valor*1.5)
    return print("Tu sueldo será: " + str(pago))
try:
    H = float(input("¿Cuántas horas trabajaste? "))
    VH = float(input("¿Cuánto te pagan por hora? "))
    computer_pay(H,VH)
except:
    print("Datos incorrectos")
