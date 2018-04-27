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
caracteristica = db.labels.create("Caracteristica")
regalo = db.labels.create("Regalos")

#gusto = "Videojuegos"

def obtenerRegalo(caracteristica):        
    
    q = 'MATCH (u:Caracteristica)-[r:a]->(m:Regalos) WHERE u.name="'+caracteristica+'" RETURN u, type(r), m'

    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:       
        #print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))

        return r[2]["name"]

def obtenerPrecio(regalito):
    
    q = 'MATCH (u:Caracterista)-[r:b]->(m:Regalos) WHERE m.name="'+regalito+'" RETURN u, type(r), m'

    results = db.query(q, returns=(client.Node, str, client.Node))
    for r in results:      
        print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))

        return r[2]["name"]

def asignarPuntos(caracteristica,Diccionario,regalo):    

    ptos = caracteristica

    if(regalo in Diccionario):            
        ptosActuales = Diccionario[regalo[1]]
        ptosActuales = ptosActuales + ptos
        
        Diccionario.insert(regalo[1],ptosActuales)
        
    else:

        #precio = obtenerPrecio(regalo)
        
        Diccionario[regalo] = []
        Diccionario[regalo].append(ptos)
        Diccionario[regalo].append(200)                

    return Diccionario
    
