def computepay(x):
    if x<=40:
        y= x*10.5
    else:
        y=(x-40)*15.75+x*10.5
    return y

print('Calcularemos cuanto dinero debe recibir  ')

a= float(input('Ingresa numero de horas trabajadas a la semana'))


print(computepay(a))
