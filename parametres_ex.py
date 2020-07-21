def saludo(idioma):
    if idioma == "En" :
            print("Hello")
    elif idioma == "Fr" :
        print ("Bonjour")
    elif idioma == "Es" :
        print("Hola")
    else :
        print("No es un idioma")

Entrada=input("Ingrese el idioma del saludo (En, Fr, Es):")

saludo(Entrada)
