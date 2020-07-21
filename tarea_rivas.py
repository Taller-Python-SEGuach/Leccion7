minimo = 40
xhora = float(input("cuanto gana por hora :"))
def computepay(horas):
    if horas > 40:
        print((horas-minimo)*1.5*xhora + minimo*xhora)
    else:
        print(horas*xhora)
input = input("cuantas horas trabajo :")
computepay(float(input))
