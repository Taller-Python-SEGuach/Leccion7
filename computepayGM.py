def computepay(x,z):
    if x<=40:
        y= x*z
    else:
        y=(x-40)*z*1.5+x*z
    return y

print('Calcularemos cuanto dinero debe recibir  ')

a= float(input('Ingresa numero de horas trabajadas a la semana'))
b= float(input('Ingresa valor de tu hora de trabajo'))

print(computepay(a,b))
