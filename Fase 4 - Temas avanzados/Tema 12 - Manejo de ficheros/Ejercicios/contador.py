import sys

with open("contador.txt","a+",encoding="utf8") as txtfile:
    txtfile.seek(0)
    contenido = txtfile.readline()

    if len(contenido) == 0:
        contenido = "0"
        txtfile.write(contenido)
        print("Se crea el fichero contador.txt")

    else:
        
        try:
            contador = int(contenido)
        
        except:
            print("Error: Fichero corrupto")

        else:
            try:
                argumento = sys.argv[1]
            except:
                print("No se envía argumento incremental o decremental")
            else:
                print(f"Incialmente el contador está a {contador}")
                if sys.argv[1] == "inc":
                    contador += 1
                elif sys.argv[1] == "dec":
                    contador -= 1
            
            print(f"El contador está a {contador}")
            txtfile.seek(0)
            txtfile.truncate()
            txtfile.write(str(contador))
    
    txtfile.close()


