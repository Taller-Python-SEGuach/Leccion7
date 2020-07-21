def sumar(a,b):
    c = a + b
    return c

print("sumaremos 2 numeros enteros")

x=input("Ingrese el primer numero: ")
y=input("Ingrese el segundo numero: ")

try :
   x = int(x)
   y = int(y)
   sumar(x,y)
   print("el resultado de la suma es", sumar(x,y))
except :
    print("no ingreso un numero entero")
