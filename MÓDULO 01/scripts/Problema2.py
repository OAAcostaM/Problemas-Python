import re
abecedario_mayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
abecedario_minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
clave = input("Introduza las letras clave: ")
longitud_clave = len(clave)
encriptado = list()
if len(clave) == 27 :
    palabra = input("Introduzca la palabra a encriptar: ")
    cont = 0
    for i in range(len(palabra)) :
        if re.findall(r"[A-Z]",palabra[cont]) or clave[cont] == "Ñ" :
            indice_mayus = abecedario_mayus.index(palabra[cont])
            encriptado.append(clave[indice_mayus])
        if re.findall(r"[a-z]",palabra[cont]) or clave[cont] == "ñ" :
            indice_minus = abecedario_minus.index(palabra[cont])
            encriptado.append(clave[indice_minus])
        if re.findall(r"\s",palabra[cont]) :
            encriptado.append(" ")
        if palabra[cont] == "," :
            encriptado.append(",") 
        if palabra[cont] == "." :
            encriptado.append(".") 
        cont += 1
else :
    print("La clave no tiene 27 letras")
    
print("La palabra encriptada es: {}".format(encriptado))
listado = "".join(encriptado)
print("Cadena :",listado)
