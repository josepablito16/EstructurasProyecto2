# Universidad del Valle de Guatemala
# Algoritmos y estructura de datos
# Proyecto 2: Sistema de Recomendaciones
#Fecha: XX/05/2018
# Colaboradores:
    # Javier Carpio - 17077
    # Jose Cifuenres - 17509
    # Oscar Juarez - 17315

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client


db = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")
manager = Neo4jDBSessionManager(settings.NEO4J_RESOURCE_URI, settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)

caracteristica = db.labels.create("Caracteristica")
regalo = db.labels.create("Regalos")

#gusto = "Videojuegos"

def obtenerRegalo(caracteristica,diccionario,puntos):        
    
    q = 'MATCH (u:Caracteristica)-[r:a]->(m:Regalos) WHERE u.name="'+caracteristica+'" RETURN u, type(r), m'

    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:       
        print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))

        if(r[2]["name"] in diccionario):
            #se le suman puntos
            diccionario[r[2]["name"]].insert(0,diccionario[r[2]["name"]][0]+puntos)
            diccionario[r[2]["name"]].pop(1)
            print("entro")
            
        else:
            #se agrega al diccionario
            l= 'MATCH (u:Regalos)-[r:b]->(m:Caracteristica) WHERE u.name="'+r[2]["name"]+'" RETURN u, type(r), m'
            results = db.query(l, returns=(client.Node, str, client.Node))
            for l in results:       
                diccionario[r[2]["name"]]=[puntos,l[2]["name"]]
            
        
    return diccionario

def getSugerencias(diccionario,precio):
    nuevo={}
    for i in diccionario:
        print("precio"+diccionario[i][1])
        if(diccionario[i][1]==precio):
            print("Entro")
            nuevo[i]=diccionario[i][0]

    print(nuevo)
    
    diccionarioLista=[]
        
    for i in nuevo.values():
        diccionarioLista.append(i)

    diccionarioLista.sort(reverse=True)
    print(diccionarioLista)

    sugerencia=[]
    for x in nuevo:
        if(nuevo[x]==diccionarioLista[0]):
            diccionarioLista.pop(0)
            sugerencia.append(x)

    print(sugerencia)
    return sugerencia
