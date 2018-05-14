from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:11007", username="neo4j", password="mypassword")
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
Musica = db.nodes.create(name="Musica")
Fiestas = db.nodes.create(name="Fiestas")
Entretenimiento = db.nodes.create(name="Entretenimiento")
Estudios = db.nodes.create(name="Estudios")
Viajes = db.nodes.create(name="Viajes")
Aventuras = db.nodes.create(name="Aventuras")
Deportes = db.nodes.create(name="Deportes")
Activo = db.nodes.create(name="Activo")

caracteristica.add(Videojuegos,Amigo,Hombre,Celebración,Introvertido,Medio,Extrovertido,Alto,Nolosé,Muycercana,Mujer,Importante,Decoración,Estilo)
caracteristica.add(Casual,Bajo,Cualquiera,Muycercano,Comida,Conocido,Musica,Fiestas,Entretenimiento,Estudios,Viajes,Aventuras,Deportes,Activo)

# 1

u1 = db.nodes.create(name="Coleccionable", popularidad = "8")
regalo.add(u1)
 
Videojuegos.relationships.create("a", u1)
Amigo.relationships.create("a", u1)
Hombre.relationships.create("a", u1)
Celebración.relationships.create("a", u1)
Introvertido.relationships.create("a", u1)
u1.relationships.create("b", Medio)

# 2
u2 = db.nodes.create(name="Camisa formal", popularidad = "8")
regalo.add(u2)

Estilo.relationships.create("a", u2)
Celebración.relationships.create("a", u2)
Hombre.relationships.create("a", u2)
Muycercana.relationships.create("a", u2)
Extrovertido.relationships.create("a", u2)
u2.relationships.create("b",Alto)

# 3

u3 = db.nodes.create(name="Peluche de felpa", popularidad = "7")
regalo.add(u3)

Nolosé.relationships.create("a", u3)
Muycercana.relationships.create("a", u3)
Mujer.relationships.create("a", u3)
Importante.relationships.create("a", u3)
Introvertido.relationships.create("a", u3)
u3.relationships.create("b",Medio)

# 4

u4 = db.nodes.create(name="Taza con mensaje especial", popularidad = "6")
regalo.add(u4)

Decoración.relationships.create("a", u4)
Muycercana.relationships.create("a", u4)
Mujer.relationships.create("a", u4)
Casual.relationships.create("a", u4)
Introvertido.relationships.create("a", u4)
u4.relationships.create("b", Bajo)

# 5

u5= db.nodes.create(name="Brazalete", popularidad = "7")
regalo.add(u5)

Estilo.relationships.create("a", u5)
Amigo.relationships.create("a", u5)
Cualquiera.relationships.create("a", u5)
Celebración.relationships.create("a", u5)
Extrovertido.relationships.create("a", u5)
u5.relationships.create("b",Bajo)

# 6

u6= db.nodes.create(name="Invitación a comer", popularidad = "5")
regalo.add(u6)

Comida.relationships.create("a", u6)
Amigo.relationships.create("a", u6)
Cualquiera.relationships.create("a", u6)
Importante.relationships.create("a", u6)
Extrovertido.relationships.create("a", u6)
u6.relationships.create("b", Medio)


# 7

u7= db.nodes.create(name="Bolsa de dulces", popularidad = "6")
regalo.add(u7)

Comida.relationships.create("a", u7)
Muycercana.relationships.create("a", u7)
Cualquiera.relationships.create("a", u7)
Casual.relationships.create("a", u7)
Introvertido.relationships.create("a", u7)
u7.relationships.create("b", Bajo)

# 8

u8= db.nodes.create(name="Cosméticos", popularidad = "10")
regalo.add(u8)

Estilo.relationships.create("a", u8)
Muycercana.relationships.create("a", u8)
Mujer.relationships.create("a", u8)
Celebración.relationships.create("a", u8)
Extrovertido.relationships.create("a", u8)
u8.relationships.create("b", Medio)

# 9

u9= db.nodes.create(name="Cupon de descuento", popularidad = "10")
regalo.add(u9)

Nolosé.relationships.create("a", u9)
Amigo.relationships.create("a", u9)
Cualquiera.relationships.create("a", u9)
Casual.relationships.create("a", u9)
Extrovertido.relationships.create("a", u9)
u9.relationships.create("b", Medio)

# 10

u10= db.nodes.create(name="Billetera", popularidad = "7")
regalo.add(u10)

Estilo.relationships.create("a", u10)
Conocido.relationships.create("a", u10)
Hombre.relationships.create("a", u10)
Celebración.relationships.create("a", u10)
Extrovertido.relationships.create("a", u10)
u10.relationships.create("b", Alto)

# 11

u11= db.nodes.create(name="Retrato", popularidad = "7")
regalo.add(u11)

Decoración.relationships.create("a", u11)
Muycercano.relationships.create("a", u11)
Cualquiera.relationships.create("a", u11)
Importante.relationships.create("a", u11)
Introvertido.relationships.create("a", u11)
u11.relationships.create("b", Medio)

#12 - Audifonos

u12= db.nodes.create(name="Audífonos", popularidad = "8")
regalo.add(u12)

Musica.relationships.create("a", u12)
Amigo.relationships.create("a", u12)
Cualquiera.relationships.create("a", u12)
Celebración.relationships.create("a", u12)
Introvertido.relationships.create("a", u12)
u12.relationships.create("b", Medio)

#13 - Losion

u13= db.nodes.create(name="Losión", popularidad = "6")
regalo.add(u13)

Fiestas.relationships.create("a", u13)
Muycercano.relationships.create("a", u13)
Hombre.relationships.create("a", u13)
Celebración.relationships.create("a", u13)
Extrovertido.relationships.create("a", u13)
u13.relationships.create("b", Alto)


#14 - Juego de mesa

u14= db.nodes.create(name="Juego de mesa", popularidad = "7")
regalo.add(u14)

Entretenimiento.relationships.create("a", u14)
Amigo.relationships.create("a", u14)
Cualquiera.relationships.create("a", u14)
Celebración.relationships.create("a", u14)
Extrovertido.relationships.create("a", u14)
u14.relationships.create("b", Medio)

#15 - Corbata formal

u15= db.nodes.create(name="Corbata formal", popularidad = "6")
regalo.add(u15)

Fiestas.relationships.create("a", u15)
Estilo.relationships.create("a", u15)
Conocido.relationships.create("a", u15)
Hombre.relationships.create("a", u15)
Celebración.relationships.create("a", u15)
Extrovertido.relationships.create("a", u15)
u15.relationships.create("b", Medio)

#16 - Guitarra

u16= db.nodes.create(name="Guitarra", popularidad = "10")
regalo.add(u16)

Musica.relationships.create("a", u16)
Muycercano.relationships.create("a", u16)
Cualquiera.relationships.create("a", u16)
Importante.relationships.create("a", u16)
Introvertido.relationships.create("a", u16)
u16.relationships.create("b", Alto)

#17 - Losion

u17= db.nodes.create(name="Mochila", popularidad = "8")
regalo.add(u17)

Estudios.relationships.create("a", u17)
Aventuras.relationships.create("a", u17)
Viajes.relationships.create("a", u17)
Muycercano.relationships.create("a", u17)
Cualquiera.relationships.create("a", u17)
Celebración.relationships.create("a", u17)
Introvertido.relationships.create("a", u17)
u17.relationships.create("b", Alto)

#18 - Gorra

u18= db.nodes.create(name="Gorra", popularidad = "6")
regalo.add(u18)

Estilo.relationships.create("a", u18)
Conocido.relationships.create("a", u18)
Hombre.relationships.create("a", u18)
Casual.relationships.create("a", u18)
Extrovertido.relationships.create("a", u18)
u18.relationships.create("b", Alto)

#19 - Fidget Spinner

u19= db.nodes.create(name="Fidget Spinner", popularidad = "4")
regalo.add(u19)

Entretenimiento.relationships.create("a", u19)
Conocido.relationships.create("a", u19)
Cualquiera.relationships.create("a", u19)
Casual.relationships.create("a", u19)
Introvertido.relationships.create("a", u19)
u19.relationships.create("b", Bajo)

#20 - Tennis

u20= db.nodes.create(name="Tennis", popularidad = "9")
regalo.add(u20)

Deportes.relationships.create("a", u20)
Muycercano.relationships.create("a", u20)
Cualquiera.relationships.create("a", u20)
Importante.relationships.create("a", u20)
Activo.relationships.create("a", u20)
u20.relationships.create("b", Alto)

#21 - Pelota de futbol

u21= db.nodes.create(name="Pelota de futbol", popularidad = "8")
regalo.add(u21)

Deportes.relationships.create("a", u21)
Amigo.relationships.create("a", u21)
Hombre.relationships.create("a", u21)
Celebración.relationships.create("a", u21)
Activo.relationships.create("a", u21)
u21.relationships.create("b", Medio)

#22 - Caja de chocolates

u22= db.nodes.create(name="Caja de chocolates", popularidad = "8")
regalo.add(u22)

Comida.relationships.create("a", u22)
Muycercano.relationships.create("a", u22)
Mujer.relationships.create("a", u22)
Importante.relationships.create("a", u22)
Introvertido.relationships.create("a", u22)
u22.relationships.create("b", Medio)

#23 - Ramo de flores

u23= db.nodes.create(name="Ramo de flores", popularidad = "6")
regalo.add(u23)

Decoración.relationships.create("a", u23)
Muycercano.relationships.create("a", u23)
Mujer.relationships.create("a", u23)
Importante.relationships.create("a", u23)
Introvertido.relationships.create("a", u23)
u23.relationships.create("b", Bajo)

#24 - Juego de aretes

u24= db.nodes.create(name="Juego de aretes", popularidad = "8")
regalo.add(u24)

Estilo.relationships.create("a", u24)
Amigo.relationships.create("a", u24)
Mujer.relationships.create("a", u24)
Celebración.relationships.create("a", u24)
Extrovertido.relationships.create("a", u24)
u24.relationships.create("b", Alto)

#25 - Llavero

u25= db.nodes.create(name="Llavero", popularidad = "4")
regalo.add(u25)

Decoración.relationships.create("a", u25)
Amigo.relationships.create("a", u25)
Mujer.relationships.create("a", u25)
Casual.relationships.create("a", u25)
Introvertido.relationships.create("a", u25)
u25.relationships.create("b", Bajo)

#26 - Camisola de equipo

u26= db.nodes.create(name="Camisola de equipo", popularidad = "8")
regalo.add(u26)

Deportes.relationships.create("a", u26)
Amigo.relationships.create("a", u26)
Hombre.relationships.create("a", u26)
Celebración.relationships.create("a", u26)
Activo.relationships.create("a", u26)
u26.relationships.create("b", Medio)

#27 - Silla portatil

u27= db.nodes.create(name="Silla portatil", popularidad = "7")
regalo.add(u27)

Aventuras.relationships.create("a", u27)
Amigo.relationships.create("a", u27)
Hombre.relationships.create("a", u27)
Celebración.relationships.create("a", u27)
Extrovertido.relationships.create("a", u27)
u27.relationships.create("b", Medio)

#28 - Bocinas

u28= db.nodes.create(name="Bocinas", popularidad = "10")
regalo.add(u28)

Musica.relationships.create("a", u28)
Amigo.relationships.create("a", u28)
Cualquiera.relationships.create("a", u28)
Celebración.relationships.create("a", u28)
Extrovertido.relationships.create("a", u28)
u28.relationships.create("b", Medio)

#29 - Boletos de avión

u29= db.nodes.create(name="Boletos de avion", popularidad = "10")
regalo.add(u29)

Viajes.relationships.create("a", u29)
Aventuras.relationships.create("a", u29)
Muycercano.relationships.create("a", u29)
Cualquiera.relationships.create("a", u29)
Importante.relationships.create("a", u29)
Extrovertido.relationships.create("a", u29)
u29.relationships.create("b", Alto)

q = 'MATCH (u:caracteristica)-[r:a]->(m:regalo) WHERE u.name="Ropa" RETURN u, type(r), m'

results = db.query(q, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
