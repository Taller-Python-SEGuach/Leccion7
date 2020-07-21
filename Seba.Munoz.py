def computepay(horas,pago):
    if horas>=40.0:
        x=(horas-40.0)
        c=((x*pago*1.5)+(40.0*pago))
    else:
        c=(horas*pago)
    print( "Ganaras "+ str(c),"morlacos" )

try:
    a = float(input("ingrese horas de trabajo "))
    b = float(input("ingrese pago por hora "))
    computepay(a,b)
except:
    print("malito")
