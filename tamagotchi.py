#=== Imports ===#
import random
import time
import datetime
import threading

# === clases === #
class tamagotchi:
    def __init__(self, nombre, felicidad, hambre, tipo, peso):
        self.nombre = nombre
        self.felicidad = felicidad
        self.hambre  = hambre
        self.tipo = tipo
        self.peso = peso

    # Metodos de la clase
    def dormir(self):
        pass

    def jugar(self):
        eleccion= input()
        pass

    def nombrar(self):
        nombre=input("Ingrese su nombre: ")
        self.nombre = nombre
        return f"Tu nombre es: {nombre}"

    def comer(self):
        pass

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}\nFelicidad: {self.felicidad}\nHambre: {self.hambre}\nPeso: {self.peso}\nTipo: {self.tipo}")

    def limpiar(self):
        pass

    def cagar(self):
        pass

class huevo(tamagotchi):
    def __init__(self, nombre, felicidad, hambre, tipo, peso):
        super().__init__(nombre, felicidad, hambre, tipo, peso)

class bebe(tamagotchi):
    def __init__(self, nombre, felicidad, hambre, tipo, peso):
        super().__init__(nombre, felicidad, hambre, tipo, peso)

class adolescente(tamagotchi):
    def __init__(self, nombre, felicidad, hambre, tipo, peso):
        super().__init__(nombre, felicidad, hambre, tipo, peso)

class adulto(tamagotchi):
    def __init__(self, nombre, felicidad, hambre, tipo, peso):
        super().__init__(nombre, felicidad, hambre, tipo, peso)
        
                
# === Funciones === #
def reloj(tiempo, fecha):
    while True:
        print (f"{tiempo[0]} : {tiempo[1]} : {tiempo[2]}")
        time.sleep(1)
        if tiempo[2] == 59:
            if tiempo[1] == 59:
                tiempo[0] +=1
                tiempo[1] = 0
            tiempo[1] += 1
            tiempo[2] = 0
        elif tiempo[2] < 59:
            tiempo[2] += 1
        elif tiempo[0] == 24:
            if fecha.month == 12:
                fecha.year += 1
            else:
                fecha.replace(month=fecha.month+1)

def petsPref(pets, foods, drinks):
    for name in pets:
        if name == "Mametchi":
            foods["apple"]["felicidad"] = 3
            drinks["water"]["felicidad"] = 2
        elif name == "Kuchipatchi":
            pass
        elif name == "Lovelin":
            pass
        elif name == "Memetchi":
            pass
        elif name == "Kuromametchi":
            pass
        elif name == "Gozarutchi":
            pass
        elif name == "Chamametchi":
            pass
        elif name == "Happyhappytchi":
            pass
        elif name == "Uwasatchi":
            pass
        elif name == "Kikitchi":
            pass
        elif name == "Cherry":
            pass
        elif name == "Felipoto":
            pass

def cambioFecha():
    day = input("Ingrese el día: ")
    year = input("Ingrese el año: ")
    month = input("Ingrese el mes (1-12): ")
    return year, month, day

def cambioHora(tiempo):
    tiempo[1] = input("ingrese los minutos: ")
    tiempo[0] = input("ingrese las horas: ")
    return tiempo

            
def main():
    mascota=tamagotchi(None, 75, 50, 75, random.choice(pets))
    print ("Bienvenido a Tamagotchi!")
    flag = True
    while flag:
        salir = input("s")
        if salir == "s":
            flag = False


# === Variables globales === #
pets=["Mametchi", "Kuchipatchi", "Lovelin", "Memetchi", "Kuromametchi", "Gozarutchi", "Chamametchi", "Happyhappytchi", "Uwasatchi", "Kikitchi", "Cherry", "Felipoto"]
foods = {"apple":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "banana":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "pizza":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "burger":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "fries":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "chicken":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "steak":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "salad":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "sandwich":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "taco":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "sushi":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "ramen":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "noodles":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "rice":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "eggs":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "bacon":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "pancake":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "waffles":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "ice cream":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
         "donut":{"calorias": 0, "cantidad": 0, "felicidad": 0}
         }
drinks = {"water":{"calorias": 0, "cantidad": 0, "felicidad": 0},
            "soda":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "tea":{"calorias": 0, "cantidad": 0, "felicidad": 0},
            "coffee":{"calorias": 0, "cantidad": 0, "felicidad": 0},
            "juice":{"calorias": 0, "cantidad": 0, "felicidad": 0},
            "milk":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "beer":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "wine":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "champagne":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "cocktail":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "smoothie":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "mocha":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "latte":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "cappuccino":{"calorias": 0, "cantidad": 0, "felicidad": 0}, 
            "espresso":{"calorias": 0, "cantidad": 0, "felicidad": 0}
            }

tiempo = [0,0,0]
year =  2024
month = 4
day = 26
fecha = datetime.date(year, month, day)
#year, month, day = cambioFecha()


# === Hilos ===#
hiloReloj = threading.Thread(name= "hilo_principal", target= reloj, args=(tiempo, fecha) )
hiloMascota = threading.Thread(name= "hilo_mascota", target= main)
hiloReloj.daemon = True

# === Main === #
hiloReloj.start()
hiloMascota.start()