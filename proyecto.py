from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")
caracteristica = db.labels.create("Caracteristica")
regalo = db.labels.create("Regalos")
popularidad = db.labels.create("Popularidad")

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
Decoración= db.nodes.create(name="Decoración")
Casual= db.nodes.create(name="Casual")
Bajo= db.nodes.create(name="Bajo")
Cualquiera= db.nodes.create(name="Cualquiera")
Comida= db.nodes.create(name="Comida")
Muycercano= db.nodes.create(name="Muycercano")
Conocido= db.nodes.create(name="Conocido")

caracteristica.add(Videojuegos,Amigo,Hombre,Celebración,Introvertido,Medio,Extrovertido,Alto,Nolosé,Muycercana,Mujer,Importante,Decoración,Estilo)
caracteristica.add(Casual,Bajo,Cualquiera,Muycercano,Comida,Conocido)
# 1

u1 = db.nodes.create(name="Coleccionable")
regalo.add(u1)

p1 = db.nodes.create(name="8")
popularidad.add(p1)
p1.relationships.create("c", u1)
 
Videojuegos.relationships.create("a", u1)
Amigo.relationships.create("a", u1)
Hombre.relationships.create("a", u1)
Celebración.relationships.create("a", u1)
Introvertido.relationships.create("a", u1)
u1.relationships.create("b", Medio)

# 2
u2 = db.nodes.create(name="Camisa formal")
regalo.add(u2)

p2 = db.nodes.create(name="7")
popularidad.add(p2)
p2.relationships.create("c", u2)

Estilo.relationships.create("a", u2)
Celebración.relationships.create("a", u2)
Hombre.relationships.create("a", u2)
Muycercana.relationships.create("a", u2)
Extrovertido.relationships.create("a", u2)
u2.relationships.create("b",Alto)

# 3

u3 = db.nodes.create(name="Peluche de felpa")
regalo.add(u3)

p3 = db.nodes.create(name="8")
popularidad.add(p3)
p3.relationships.create("c", u3)

Nolosé.relationships.create("a", u3)
Muycercana.relationships.create("a", u3)
Mujer.relationships.create("a", u3)
Importante.relationships.create("a", u3)
Introvertido.relationships.create("a", u3)
u3.relationships.create("b",Medio)

# 4

u4 = db.nodes.create(name="Taza con mensaje especial")
regalo.add(u4)

p4 = db.nodes.create(name="6")
popularidad.add(p4)
p4.relationships.create("c", u4)

Decoración.relationships.create("a", u4)
Muycercana.relationships.create("a", u4)
Mujer.relationships.create("a", u4)
Casual.relationships.create("a", u4)
Introvertido.relationships.create("a", u4)
u4.relationships.create("b", Bajo)

# 5

u5= db.nodes.create(name="Brazalete")
regalo.add(u5)

p5 = db.nodes.create(name="7")
popularidad.add(p5)
p5.relationships.create("c", u5)

Estilo.relationships.create("a", u5)
Amigo.relationships.create("a", u5)
Cualquiera.relationships.create("a", u5)
Celebración.relationships.create("a", u5)
Extrovertido.relationships.create("a", u5)
u5.relationships.create("b",Bajo)

# 6

u6= db.nodes.create(name="Invitación a comer")
regalo.add(u6)

p6 = db.nodes.create(name="5")
popularidad.add(p6)
p6.relationships.create("c", u6)

Comida.relationships.create("a", u6)
Amigo.relationships.create("a", u6)
Cualquiera.relationships.create("a", u6)
Importante.relationships.create("a", u6)
Extrovertido.relationships.create("a", u6)
u6.relationships.create("b", Medio)


# 7

u7= db.nodes.create(name="Bolsa de dulces")
regalo.add(u7)

p7 = db.nodes.create(name="6")
popularidad.add(p7)
p7.relationships.create("c", u7)

Comida.relationships.create("a", u7)
Muycercana.relationships.create("a", u7)
Cualquiera.relationships.create("a", u7)
Casual.relationships.create("a", u7)
Introvertido.relationships.create("a", u7)
u7.relationships.create("b", Bajo)

# 8

u8= db.nodes.create(name="Cosméticos")
regalo.add(u8)

p8 = db.nodes.create(name="10")
popularidad.add(p8)
p8.relationships.create("c", u8)

Estilo.relationships.create("a", u8)
Muycercana.relationships.create("a", u8)
Mujer.relationships.create("a", u8)
Celebración.relationships.create("a", u8)
Extrovertido.relationships.create("a", u8)
u8.relationships.create("b", Medio)

# 9

u9= db.nodes.create(name="Cupon de descuento")
regalo.add(u9)

p9 = db.nodes.create(name="10")
popularidad.add(p9)
p9.relationships.create("c", u9)

Cualquiera.relationships.create("a", u9)
Amigo.relationships.create("a", u9)
Cualquiera.relationships.create("a", u9)
Casual.relationships.create("a", u9)
Extrovertido.relationships.create("a", u9)
u9.relationships.create("b", Medio)

# 10

u10= db.nodes.create(name="Billetera")
regalo.add(u10)

p10 = db.nodes.create(name="7")
popularidad.add(p10)
p10.relationships.create("c", u10)

Estilo.relationships.create("a", u10)
Conocido.relationships.create("a", u10)
Hombre.relationships.create("a", u10)
Celebración.relationships.create("a", u10)
Extrovertido.relationships.create("a", u10)
u10.relationships.create("b", Alto)

# 11

u11= db.nodes.create(name="Retrato")
regalo.add(u11)
    
p11 = db.nodes.create(name="7")
popularidad.add(p11)
p11.relationships.create("c", u11)

Decoración.relationships.create("a", u11)
Muycercano.relationships.create("a", u11)
Cualquiera.relationships.create("a", u11)
Importante.relationships.create("a", u11)
Introvertido.relationships.create("a", u11)
u11.relationships.create("b", Medio)

q = 'MATCH (u:caracteristica)-[r:a]->(m:regalo) WHERE u.name="Ropa" RETURN u, type(r), m'

results = db.query(q, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
