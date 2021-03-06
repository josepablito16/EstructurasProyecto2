# Universidad del Valle de Guatemala
# Algoritmos y estructura de datos
# Proyecto 2: Sistema de Recomendaciones
#Fecha: XX/05/2018
# Colaboradores:
    # Javier Carpio - 17077
    # Jose Cifuenres - 17509
    # Oscar Juarez - 17315


from Implementacion import *
import webbrowser


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

        #print(Diccionario)
    

        

        #ASIGNACION DE GENEROS
        print (listaGeneros)
        genero = input("Ingrese el genero: ")

        if (genero=="1"):
            genero = "Hombre"
        elif (genero=="2"):
            genero = "Mujer"
        elif (genero == "3"):
            genero = "Indefinido"

        Diccionario = obtenerRegalo(genero,Diccionario,1)
        #print(Diccionario)
       
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
        #print(Diccionario)

        #ASIGNACION DE CERCANIA
        print (listaCercania)
        cercania = input("Ingrese la cercania: ")
        Diccionario = obtenerRegalo(cercania,Diccionario,1)
        #print(Diccionario)


        #ASIGNACION DE OCASION
        print (listaOcasion)
        ocasion = input("Ingrese la ocasion: ")
        Diccionario = obtenerRegalo(ocasion,Diccionario,1)
        #print(Diccionario)
        

        #ASIGNACION DE PERSONALIDAD
        print (listaPersonalidad)
        personalidad = input("Ingrese la personalidad de la persona: ")
        Diccionario = obtenerRegalo(personalidad,Diccionario,1)
        #print(Diccionario)

                    
        # devuelve una lista con los nombres de los regalos del mayor puntaje al menor
        listaSugerencias=getSugerencias(Diccionario,dinero)
        
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")

        if(len(listaSugerencias) > 0):
            imprimarListaReg(listaSugerencias)
        else:
            print("No hemos podido encontrar coincidencias\n")

        url1 = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="
        seleccionRegalo=int(input("Ayudenos a mejorar, indique el numero de regalo escogio: "))
        print(listaSugerencias[seleccionRegalo-1])
        url = url1 + listaSugerencias[seleccionRegalo-1]

        puntuacionRegalo=int(input("Valore el regalo con una puntuacion de 1 a 10: "))
        
        actualizarPuntuacion(listaSugerencias[seleccionRegalo-1],puntuacionRegalo)
        
        webbrowser.open_new(url)
    else:
        print("\nGracias por utilizar este sistema de recomendacion :)\n")
        break
        
