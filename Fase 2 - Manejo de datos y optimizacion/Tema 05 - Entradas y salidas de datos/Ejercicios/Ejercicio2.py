import sys

if len(sys.argv) != 3:
    print("Debe introducir 2 valores")
else:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    for i in range(filas):
        for j in range(columnas):
            print(" * ", end = '')
        print("")

