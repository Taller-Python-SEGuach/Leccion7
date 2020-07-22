def computepay (x,y):
    #Cuanto ganarás por la semana de trabajo

    if x<=40 :
        z=x*y

    else:
        z =(40*y) + ((x - 40)*y*1.5)
    return print ("Cuanto ganarás por la semana de trabajo :" + str (z))

try:
    x = float(input("ingrese cuantas horas trabajas a la semana:"))
    y = float(input("ingrese cuanto ganas por hora:"))
    computepay(x,y)

except:
    print("Error")
