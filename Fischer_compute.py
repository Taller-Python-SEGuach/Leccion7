def compute_1(a,b):
    c=(a-40)*(1.5*b)
    return c

def compute_2(b):
    c=40*b
    return c

def compute_3(a,b):
    c=a*b
    return c

print("Calculo de ganancia total por horas trabajadas")

x=input("ingrese horas trabajadas:")
y=input("ingrese ganancia por hora:")

try:
    x=float(x)
    y=float(y)

    if x > 40:
        compute_1(x,y)+compute_2(y)
        print("la ganancia total es:",compute_1(x,y)+compute_2(y))
    else:
        compute_3(x,y)
        print(compute_3(x,y))
        print("la ganancia total es:", compute_3(x,y))
except:
    print("los numeros ingresados no son validos")

    
