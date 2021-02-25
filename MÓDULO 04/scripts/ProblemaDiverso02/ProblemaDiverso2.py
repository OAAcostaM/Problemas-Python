"""
2.
Escribir una función que pida un número entero entre 1 y 10, 
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
done n es el número introducido, y la muestre por pantalla. 
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""

def comprobacion_rango (num) :
    if num > 0 and num <= 10 :
        return True
    return False

def validacion () :
    bandera = False
    while bandera == False :
        while True :
            try :
                n = int(input("Digite un número entre 1 y 10: "))
            except :
                print("Ha ocurrido un error, introduce bien el número")
            else :
                break
        bandera = comprobacion_rango(n)
    
    return n

numero = validacion()

while True :
    try :
        fichero = open('./src/tabla-n.txt','r+') 
        fichero.close()
        
        with open('./src/tabla-n.txt','w') as f :
            
            number = "El número es: {}\n".format(numero)
            f.write(number)
            
            for i in range(1,11) :
                texto = "{} x {} = {}\n".format(numero,i,(i*numero))
                f.write(str(texto))
                
        with open('./src/tabla-n.txt','r') as f :
            for linea in f :
                print(linea)
    except :
        print("Ha ocurrido un error, fichero no encontrado")
        break
    else :
        break