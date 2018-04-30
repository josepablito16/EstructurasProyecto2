# Universidad del Valle de Guatemala
# Algoritmos y estructura de datos
# Proyecto 2: Sistema de Recomendaciones
#Fecha: XX/05/2018
# Colaboradores:
    # Javier Carpio - 17077
    # Jose Cifuenres - 17509
    # Oscar Juarez - 17315


from Implementacion import *


#___________Declaracion de variables__________#

menu = "\nLa lista de funciones es:\n1. Recomendar un regalo\n2. Salir del programa"
rangoPresupuesto = "\nEl rango de los presupuestos son:\n1. Bajo (De Q10 - Q100)\n2. Medio (De Q110 - Q500)\n3. Alto (Q510 +)"
listaGeneros = "\nLos generos disponibles son: \n1. Hombre \n2. Mujer \n3. Indefinido"
listaGustos = "\nLa lista de gustos es: \n1. Estilo \n2. Decoracion \n3. Musica \n4. Deportes \n5. Videojuegos \n6. Entretenimiento \n7. Comida \n8. Aventuras"
listaCercania = "\nQue tan cercana es la persona? \n1. Conocido \n2. Amigo \n3. Muy cercano"
listaPersonalidad = "\nComo describiria la personalidad de la persona? \n1. Introvertido \n2. Extrovertido \n3. Activo"
listaOcasion = "\nCual es la ocasion del reglao? \n1. Regalo casual \n2. Regalo por celebracion \n3. Regalo de fecha/evento importante"
Diccionario = {}


#Programa principal

while True:

    print (menu)
    seleccion = input("Ingrese la accion que desea realizar: ")

    if (seleccion=="1"):

        #ASIGNACION DE PRESUPUESTO
        print (rangoPresupuesto)
        presupuesto = int(input("Ingrese se prespuesto: "))
        dinero=""
        if(presupuesto==1):
            dinero="Bajo"

        if(presupuesto==2):
            dinero="Medio"

        if(presupuesto==3):
            dinero="Alto"

        

        #ASIGNACION DE GENEROS
        print (listaGeneros)
        generos = input("Ingrese el genero: ")

        if (generos=="1"):
            genero = "Hombre"
        elif (generos=="2"):
            genero = "Mujer"
        elif (generos == "3"):
            genero = "Indefinido"

        Diccionario = obtenerRegalo(genero,Diccionario,1)
        print(Diccionario)
       
        #ASIGNACION DE GUSTOS
        print (listaGustos)
        gusto = input("Ingrese el gusto: ")
        
        if (gusto=="1"):
            gustos = "Estilo"
        elif (gusto=="2"):
            gustos = "Decoracion"
        elif (gusto == "3"):
            gustos = "Musica"
        elif (gusto == "4"):
            gustos = "Deportes"
        elif (gusto == "5"):
            gustos = "Videojuegos"
        elif (gusto == "6"):
            gustos = "Entretenimiento"
        elif (gusto == "7"):
            gustos = "Comida"
        elif (gusto == "8"):
            gustos = "Aventuras"

        Diccionario = obtenerRegalo(gustos,Diccionario,1)
        print(Diccionario)

        #ASIGNACION DE CERCANIA
        print (listaCercania)
        cercanias = input("Ingrese la cercania: ")

        if(cercanias == "1"):
            cercania = "Conocido"
        elif(cercanias == "2"):
            cercania = "Amigo"
        elif(cercanias == "3"):
            cercania = "Muy cercano"

        #Diccionario = obtenerRegalo(cercania,Diccionario,1)
        #print(Diccionario)
        
        #ASIGNACION DE OCASION
        print (listaOcasion)
        ocasiones = input("Ingrese la ocasion: ")

        if(ocasiones == "1"):
            ocasion = "Casual"
        elif(ocasiones == "2"):
            ocasion = "Celebracion"
        elif(ocasiones == "3"):
            ocasion = "Importante"        

        #Diccionario = obtenerRegalo(ocasion,Diccionario,1)
        #print(Diccionario)

        #ASIGNACION DE PERSONALIDAD
        print (listaPersonalidad)
        personalidades = int(input("Ingrese la personalidad de la persona: "))
        personalidad = ""
        if(personalidades == 1):
            per = "Introvertido"
        elif(personalidades == 2):
            per = "Extrovertido"
        elif(personalidades == 3):
            per = "Activo"

        #Diccionario = obtenerRegalo(personalidad,Diccionario,1)
        #print(Diccionario)


        #Muestra lo que el usuario selecciono
        print("\n--------------------\nUsted selecciono:\n"
              + "Presupuesto: " + dinero
              + "\nGenero: " + genero
              + "\nGustos: " + gustos
              + "\nCercania: " + cercania
              + "\nOcasion: " + ocasion
              + "\nPersonalidad: " + per
              + "\n------------------\n")
        
        # devuelve una lista con los nombres de los regalos del mayor puntaje al menor
        sugerencias = getSugerencias(Diccionario,dinero)

        for i in sugerencias:
            resultado = getPopularidad(i)
            print (i + " -> " + resultado)
        
    else:
        print("Gracias por usar este sistema de recomendacion")
        break;


        
        
        
