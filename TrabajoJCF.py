def computepay(x,y):
    if x<=40:
        Sueldo = x * y
    else:
        Sueldo = (x-40) * y * 1.5 + (40 * y)
    return print('Calcularemos cuanto dinero debe recibir  '+ str(Sueldo))
try:
    a= float(input('Ingresa numero de horas trabajadas a la semana '))
    b= float(input('Ingresa valor de tu hora de trabajo '))
    computepay(a,b)

except:
    print("Los datos ingresados son incorrectos")
