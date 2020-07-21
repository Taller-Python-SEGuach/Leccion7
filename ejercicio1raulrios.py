#x resultado final
#h horas ingresadas
#p valor por hora ingresada
#c cantidad de horas extras

def computepay(h,p):
    x=0.0
    if(h>40):
        c=h-40            
        x=(40*p)+(c*(p*1.5))
    elif(h<=40):
        x=h*p
    return x

#ht horas trabajadas
#ph precio por hora
try:
    ht=float(input("Cantidad de horas trabajadas "))
    ph=float(input("Valor por hora "))
    print("Valor total",computepay(ht,ph),"por",ht,"horas trabajadas")
except:        
    print("Error")
