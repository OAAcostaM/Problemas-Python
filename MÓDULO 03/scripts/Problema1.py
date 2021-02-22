#American Express
#N° Digitos: 15
#Empieza: 34 o 37

#MasterCard
#N° Digitos: 16
#Empieza: 51, 52, 53, 54 o 55 o 22

#Visa
#N° Digitos: 13 y 16
#Empieza: 4

class TarjetaCredito :
    
    def __init__(self, numero_tarjeta) :
        self.numero_tarjeta = numero_tarjeta
        
    def entrada_datos(self) :
        if (self.numero_tarjeta >= 4*(10**12) and self.numero_tarjeta <= (5*(10**12)-1)) or (self.numero_tarjeta >= 4*(10**15) and self.numero_tarjeta <= (5*(10**15)-1)) :
            nombre_Tarjeta = "VISA"
        elif (self.numero_tarjeta >= 34*(10**13) and self.numero_tarjeta <= (35*(10**13)-1)) or (self.numero_tarjeta >= 37*(10**13) and self.numero_tarjeta <= (38*(10**13)-1)) :
            nombre_Tarjeta = "AMEX" 
        elif (self.numero_tarjeta >= 22*(10**14) and self.numero_tarjeta <= (23*(10**14)-1)) or (self.numero_tarjeta >= 51*(10**14) and self.numero_tarjeta <= (56*(10**14)-1)) :
            nombre_Tarjeta = "MASTERCAD"
        else :
            nombre_Tarjeta = "--*INVÁLIDO*--\n\t\t\tNúmero de tarjeta incorrecto"
                    
        return nombre_Tarjeta
    
    def comprobacion(self) :
        cadena = str(self.numero_tarjeta)
        lista = list()
        cont = 0
        cont1 = -2
        cont2 = -1
        for i in range (len(cadena)) :
            lista.append(int(cadena[cont]))
            cont += 1
        suma = 0
        if len(lista) % 2 != 0 :
            for indice in range (int(len(lista)/2)) :
                prod = lista[cont1]*2
                if prod >= 10 :
                    sum_digito = 1 + (prod%10)
                else :
                    sum_digito = prod
                suma = suma + sum_digito
                cont1 -= 2
            suma_otro = 0    
            for index in range (int(len(lista)/2)+1) :
                suma_otro += lista[cont2]
                cont2 -= 2
        else :
            for indice in range (int(len(lista)/2)) :
                prod = lista[cont1]*2
                if prod >= 10 :
                    sum_digito = 1 + (prod%10)
                else :
                    sum_digito = prod
                suma = suma + sum_digito
                cont1 -= 2
            suma_otro = 0    
            for index in range (int(len(lista)/2)) :
                suma_otro += lista[cont2]
                cont2 -= 2
        suma_total = suma + suma_otro
        if suma_total % 10 == 0 :
            valido = "*TARJETA VÁLIDA*"
        else :
            valido = "*TARJETA INVÁLIDA*"
        
        return valido
                        
    def __str__(self) :
        return "\nNumero de tarjeta: "+str(self.numero_tarjeta)
    
band = False 
while band == False :
    num_Tarjeta = int(input("Digite el número de tarjeta: "))
    if num_Tarjeta > 0 :
        band = True
        break
    print("Vuelva a ingresar su número de tarjeta")

tarjeta = TarjetaCredito(num_Tarjeta)
print(tarjeta)
print("Nombre de la tarjeta : {}".format(tarjeta.entrada_datos()))
print(tarjeta.comprobacion())