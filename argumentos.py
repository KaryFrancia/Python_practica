import sys
print(sys.argv)

cadena = sys.argv[1]
repeticiones = int(sys.argv[2])
for repeticion in   range(repeticiones):
    print(cadena)

# Comprobación de seguridad, ejecutar sólo si se reciben 2 argumentos reales
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Error - Introduce los argumentos correctamente por favor")
    print('Ejemplo: escribir_lineas.py "Texto" 5')