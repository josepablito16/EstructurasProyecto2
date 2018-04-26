from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")
caracteristica = db.labels.create("Caracteristica")
regalo = db.labels.create("Regalos")

##TODAS LAS CARACTERISTICAS
Videojuegos= db.nodes.create(name="Videojuegos")
Amigo= db.nodes.create(name="Amigo")
Hombre = db.nodes.create(name="Hombre")
Celebración = db.nodes.create(name="Celebración")
Introvertido = db.nodes.create(name="Introvertido")
Medio= db.nodes.create(name="Medio")
Estilo = db.nodes.create(name="Estilo")
Extrovertido= db.nodes.create(name="Extrovertido")
Alto= db.nodes.create(name="Alto")
Nolosé= db.nodes.create(name="No lo sé")
Muycercana= db.nodes.create(name="Muy cercana")
Mujer= db.nodes.create(name="Mujer")
Importante= db.nodes.create(name="Importante")

caracteristica.add(Videojuegos,Amigo,Hombre,Celebración,Introvertido,Medio,Extrovertido,Alto,Nolosé,Muycercana,Mujer,Importante)
 
# 1

u1 = db.nodes.create(name="Coleccionable")
regalo.add(u1)
 
Videojuegos.relationships.create("a", u1)
Amigo.relationships.create("a", u1)
Hombre.relationships.create("a", u1)
Celebración.relationships.create("a", u1)
Introvertido.relationships.create("a", u1)
Medio.relationships.create("b", u1)

# 2
u2 = db.nodes.create(name="Camisa formal")
regalo.add(u2)

Estilo.relationships.create("a", u2)
Celebración.relationships.create("a", u2)
Hombre.relationships.create("a", u2)
Muycercana.relationships.create("a", u2)
Extrovertido.relationships.create("a", u2)
Alto.relationships.create("b", u2)

# 3

u3 = db.nodes.create(name="Peluche de felpa")
regalo.add(u3)

Nolosé.relationships.create("a", u3)
Muycercana.relationships.create("a", u3)
Mujer.relationships.create("a", u3)
Importante.relationships.create("a", u3)
Introvertido.relationships.create("a", u3)
Medio.relationships.create("b", u3)




q = 'MATCH (u:Regalos)-[r:legusta]->(m:Emociones) WHERE u.name="Ropa" RETURN u, type(r), m'

results = db.query(q, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
