import io
import pickle

class Gestor:
    def __init__(self):
        print("Se inicializa el Gestor")

class Personaje:

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        try:
            print("Se inicializa la creación de Personaje")
            isinstance(nombre,str) and isinstance(vida,int) and isinstance(ataque,int) and isinstance(defensa,int) and isinstance(alcance,int)
        except:
            print("Introduzca valores válidos para: nombre, vida, ataque, defensa y alcance")
        else: 
            if vida > 0 and ataque > 0 and defensa > 0 and alcance > 0:
                self.nombre = nombre
                self.vida = vida
                self.ataque = ataque
                self.defensa = defensa
                self.alcance = alcance
            else:
                print("Introduzca valores mayores que 0")

    def __str__(self):
        return f"""Nombre = {nombre}
        Vida = {vida}
        Ataque = {ataque}
        Defensa = {defensa}
        Alcance = {alcance}"""

        