import sys

if len(sys.argv) == 2 and int(sys.argv[1]) >= 0:
    n = int(sys.argv[1])
    l = len(sys.argv[1])
    for i in range(l):
        print(f"{(n%(10**(i+1))-n%(10**i)):0{l}}")

else:
    print("Introduzca un número entero positivo")


