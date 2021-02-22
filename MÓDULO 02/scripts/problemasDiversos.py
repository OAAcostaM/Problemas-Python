#Problema Diverso 01
def evaluar_nota1(not1) :
    if nota1 >= 0 and nota1 <= 10 :
        return True
    return False

def evaluar_nota2(not2) :
    if nota2 >= 0 and nota2 <= 10 :
        return True
    return False

def evaluar_nota3(not3) :
    if nota3 >= 0 and nota3 <= 10 :
        return True
    return False

def llenado_datos(nomb, not1, not2, not3,contador) :
    alumno = {
        'Alumno {}'.format(contador) : nomb.upper(),
        'Nota1' : not1,
        'Nota2' : not2,
        'Nota3' : not3
    }
    return alumno

cant = int(input("Digite la cantidad de alumnos: "))
lista = list()
alumno = {}
cont = 1
for i in range(1,cant+1) :
    nombre = input("\nNombre completo de alumno {}: ".format(cont))
    bandera_nota1 = False
    bandera_nota2 = False
    bandera_nota3 = False
    while bandera_nota1 == False :
        nota1 = float(input("Nota1 del alumno: "))
        bandera_nota1 = evaluar_nota1(nota1)
    while bandera_nota2 == False :
        nota2 = float(input("Nota2 del alumno: "))
        bandera_nota2 = evaluar_nota2(nota2)
    while bandera_nota3 == False :
        nota3 = float(input("Nota3 del alumno: "))
        bandera_nota3 = evaluar_nota3(nota3)
    alumno_diccionario = llenado_datos(nombre,nota1,nota2,nota3,cont)
    lista.append(alumno_diccionario) 
    cont += 1
print(lista)

#Problema Diverso 02#Lista      
def promedio_alumno(lista_alumno) :
   promedio = list()
   for index, valor in enumerate(lista_alumno) :
       diccionario = dict(lista_alumno[index])
       suma = 0
       prom = 0
       for key, val in diccionario.items() :
           if key == "Nota1" or key == "Nota2" or key == "Nota3" :
               suma += val
       prom = suma / 3 
       promedio.append(round(prom,2))
       list(lista_alumno)
   return promedio 
   
promedio_por_alumno = promedio_alumno(lista)
print(promedio_por_alumno)
                                        #aprob,#cant
def alumno_sin_rojo(promedio_por_alumno,aprobo,cantidad) :
    for indice, valor in enumerate(promedio_por_alumno) :
        if promedio_por_alumno[indice] >= 4 :
            aprobo += 1
    return "\nDe los {} alumnos ingresados, sólo {} aprobaron".format(cantidad,aprobo)
    
aprob = 0
print(alumno_sin_rojo(promedio_por_alumno,aprob,cant))

#Problema Diverso 03                        #promedio_total,suma_total, cant  
def promedio_curso_total(promedio_por_alumno,prom_total,sum_total,cantidad) :
    for indice, valor in enumerate(promedio_por_alumno) :
        sum_total += promedio_por_alumno[indice]
    prom_total = sum_total / cantidad
    return prom_total

promedio_total = 0
suma_total = 0

print("\nEl promedio del curso total es:",round(promedio_curso_total(promedio_por_alumno,promedio_total,suma_total,cant),2))

#Problema Diverso 04
def nota_mayor(maximo, promedio_por_alumno, lista_alumno) :
    for indice, valor in enumerate(promedio_por_alumno) :
        if maximo < promedio_por_alumno[indice] :
            maximo = promedio_por_alumno[indice]
            indice_max = indice
    return indice_max

def nota_menor(minimo, promedio_por_alumno, lista_alumno) :
    for indice, valor in enumerate(promedio_por_alumno) :
        if minimo > promedio_por_alumno[indice] :
            minimo = promedio_por_alumno[indice]
            indice_min = indice
    return indice_min
    return "El alumno que sacó mayor nota es: {} \nPromedio: {}".format(lista_alumno[indice_min],promedio_por_alumno[indice_min])

maxi = 0
indice_maximo = nota_mayor(maxi, promedio_por_alumno, lista) 
print("\nEl alumno que sacó mayor nota es: {} \nPromedio: {}".format(lista[indice_maximo],promedio_por_alumno[indice_maximo]))

mini = 11
indice_minimo = nota_menor(mini, promedio_por_alumno, lista)
print("El alumno que sacó mayor nota es: {} \nPromedio: {}".format(lista[indice_minimo],promedio_por_alumno[indice_minimo]))

#Problema Diverso 05
def buscar_alumno(nomb, lista_alumno) :
    for index, valor in enumerate(lista_alumno) :
        diccionario = dict(lista_alumno[index]) 
        for key, val in diccionario.items() :
            if val == nomb :
                i = index
        list(lista_alumno)
        
    return i

name = input("\nDigite el nombre completo a buscar: ").upper()
iterador = buscar_alumno(name, lista)

print("")
print(lista[iterador])
print("Promedio: {}".format(promedio_por_alumno[iterador]))