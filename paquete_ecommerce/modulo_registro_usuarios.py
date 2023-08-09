import json

# Función para almacenar la información
def registro(dato):
  try:
    usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese la contraseña: ")
    dato.update({usuario:clave})
  except(Exception):
    print("ocurrió un error")

# Función para mostrar la información
def mostrar_registro(dato):
  try:
    print("La información almacenada en la base de datos es:")
    for usuario, clave in dato.items():
      print(f"Nombre de usuario: {usuario}, Contraseña: {clave}")
    if not dato:
      print("No hay registro almacenado")
  except(Exception):
    print("ocurrió un error")

# Función para guardar la información en un archivo de texto
def guardar_archivo(dato):
  try:
    ruta = r"C:\Users\Kary\Desktop\Python\VSCode"
    with open(ruta +r"/archivo.txt", "w") as archivo:
      json.dump(dato, archivo, indent=4)
  except(Exception):
    print("ocurrió un error")

# Función para leer la información en un archivo de texto
def leer_archivo(dato):
  try:
    ruta = r"C:\Users\Kary\Desktop\Python\VSCode"
    with open(ruta + "/archivo.txt", "r") as dato:
      contenido = dato.read()
      print(contenido)
  except(Exception):
    print("ocurrió un error")

# Función para el login de usuarios, comprobando que la contraseña coincida con el usuario
def login(dato):
  try:
    intentos = 1
    usuario_incorrecto = True
    clave_incorrecta = True

    while (usuario_incorrecto or clave_incorrecta) and intentos<=3:
      usuario = input("Ingrese el nombre de usuario: ")
      if usuario in dato:
        usuario_incorrecto = False
        clave = input("Ingrese la contraseña: ")
        if dato[usuario] == clave:
          clave_incorrecta = False
          print("Iniciaste sesión correctamente")
        else:
          print(f"Contraseña incorrecta, te quedan {3-intentos} intentos")
          intentos+=1
      else:
        print(f"Usuario incorrecto, te quedan {3-intentos} intentos")
        intentos+=1
  except(Exception):
    print("ocurrió un error")


