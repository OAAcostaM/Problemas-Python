bandera = False
while bandera == False :
    altura = int(input("Digite la altura de la pirámide: "))
    if altura >= 1 and altura <= 8 :
        for i in range(1,altura+1) :
            print(" "*(altura-i)+"#"*i)
        bandera = True