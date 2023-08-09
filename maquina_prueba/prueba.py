from paquete_ecommerce.modulo_cliente import Cliente, Cliente_suscriptor
from paquete_ecommerce.modulo_registro_usuarios import *

# Se crea los objetos
cliente1 = Cliente("Mauri", "Quintero", 36, "m_q_12@gmail.com")
cliente2 = Cliente_suscriptor("Kary", "Francia", 32, "kyfv25as32@gmail.com", 40000)
cliente3 = Cliente_suscriptor("Silvia", "Diaz", 45, "silvi_d2@hotmail.com", 35000)
cliente4 = Cliente("Carlos", "Rodriguez", 56, "c.23@hotmail.com")

# Mostrar informmación de los clientes
print(cliente1)
print(cliente2)
print(cliente3)
print(cliente4)

# Compra de los clientes
cliente1.comprar("Compupalace", "ipad", 28000)
cliente2.comprar("Tienda Inglesa", "lavadora", 12000)
cliente3.comprar("Tiendas Efe", "televisor", 40000)
cliente4.comprar("Tienda Inglesa", "cafetera", 800)

# El cliente 2 quiere canjear 2000 puntos
cliente2.canjear_punto(2000)

# Mostrar los puntos que le quedan al cliente 2
print(f"{cliente2.nombre} {cliente2.apellido} tiene {cliente2.puntos} puntos")

# El cliente 3 intenta canjear mas puntos de los que tiene
cliente3.canjear_punto(40000)