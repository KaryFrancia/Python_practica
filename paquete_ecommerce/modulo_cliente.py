class Cliente:

    def __init__(self, nombre, apellido, edad, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo

    def comprar(self, lugar, item, monto):
        print(f"{self.nombre} ha comprado {item} en la tienda {lugar} pagando un total de UYU {monto}")

    def __str__(self):
        return f"Se ha creado un nuevo cliente {self.nombre} {self.apellido} de {str(self.edad)} años, correo: {self.correo}"

class Cliente_suscriptor(Cliente):
    def __init__(self, nombre, apellido, edad, correo, puntos):
        super().__init__(nombre, apellido, edad, correo)
        self.puntos = puntos
          
    def comprar(self, lugar, item, monto):
        punto_ganado = monto/100
        self.puntos += punto_ganado
        super().comprar(lugar, item, monto)
        print(f"{self.nombre} {self.apellido} realizó una compra de UYU {monto} y ganó {punto_ganado} puntos")

    def canjear_punto(self, puntos_canje):
        if puntos_canje <= self.puntos:
            self.puntos -= puntos_canje
            print(f"{self.nombre} {self.apellido} canjeó {puntos_canje} puntos")
        else:
            print("Usted no tiene suficientes puntos para realizar el canje")
    
    def __str__(self):
        return super().__str__() + "(Suscripto al programa de puntos)"
