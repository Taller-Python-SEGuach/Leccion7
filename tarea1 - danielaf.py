def computepay(horas,valor):
    if horas>40 :
        pagototal = ((horas-(horas-40)) * valor) + (horas-40) * (valor * 1.5)
    elif horas<40 :
        pagototal = horas*valor
    return pagototal

print("¿Cuánto ganas?")
horas=float(input("Horas trabajadas :"))
valor=float(input("Valor de cada hora :"))

print("Te pagarán",computepay(horas,valor))
