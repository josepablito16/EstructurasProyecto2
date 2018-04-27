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
        presupuesto = input("Ingrese se prespuesto: ")
        

        #ASIGNACION DE GENEROS
        print (listaGeneros)
        genero = input("Ingrese el genero: ")

        if (genero=="1"):
            genero = "Hombre"
        elif (genero=="2"):
            genero = "Mujer"
        elif (genero == "3"):
            genero = "Indefinido"

        regalo = obtenerRegalo(genero)
        Diccionario = asignarPuntos(4,Diccionario,regalo)


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

        regalo = obtenerRegalo(gustos)
        Diccionario = asignarPuntos(6,Diccionario,regalo)
        

        #ASIGNACION DE CERCANIA
        print (listaCercania)
        cercania = input("Ingrese la cercania: ")


        #ASIGNACION DE OCASION
        print (listaOcasion)
        ocasion = input("Ingrese la ocasion: ")
        

        #ASIGNACION DE PERSONALIDAD
        print (listaPersonalidad)
        personalidad = input("Ingrese la personalidad de la persona: ")

                    
        print ("\nLos posibles regalos son:")
        print (Diccionario)


        
        
        
