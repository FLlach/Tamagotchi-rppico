#=== Imports ===#
import random
import time
import datetime
import threading


# === clases === #
class user:
    def __init__(self, nombre, generacion, tamapuntos):
        self.nombre = nombre
        self.generacion = generacion
        self.tamapuntos = tamapuntos

    def nombrar(self):
        nombre=input("Ingrese su nombre: ")
        self.nombre = nombre
        return f"Tu nombre es: {nombre}"
    
    def  edad_generacion(self):
        self.generacion +=1

    def agregar_puntos(self, tamapuntos):
        self.puntos += tamapuntos

class tamagotchi:
    def __init__(self, nombre, felicidad, hambre, tipo, peso, genero, mistakes, enfermo, salud, edad, etapa, llorando, caca):
        self.nombre = nombre
        self.felicidad = felicidad
        self.hambre  = hambre
        self.tipo = tipo
        self.peso = peso
        self.genero = genero
        self.mistakes = mistakes
        self.enfermo = enfermo
        self.salud = salud
        self.edad = edad
        self.etapa = etapa
        self.llorando = llorando
        self.caca = caca

    # Metodos de la clase
    def dormir(self):
        pass

    def jugar(self):
        eleccion= input()
        pass

    def nombrar(self):
        nombre=input("Ingrese su nombre: ")
        self.nombre = nombre
        return f"El nombre de tu tama es: {nombre}"

    def comer(self):
        pass

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}\nFelicidad: {self.felicidad}\nHambre: {self.hambre}\nTipo: {self.tipo}\nPeso: {self.peso}\nGenero: {self.genero}\nCare Mistakes: {self.mistakes}\nEnfermo: {self.enfermo}\nSalud: {self.salud}\nEdad: {self.edad}")

    def cagar(self):
        if self.caca == False:
            self.caca = True
        else:
            pass

    def limpiar(self):
        if self.caca ==  True:
            self.caca = False
        else: 
            pass     


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
    usuario=user(None, 1, 0)
    mascota=tamagotchi(None, 10, 75, random.choice(baby), 10, random.choice(genero), 0, False, 100, 0, etapa[0], False, False)
    print ("Bienvenido a Tamagotchi!")
    flag = True
    while flag:
        salir = input("s")
        if salir == "s":
            flag = False

def menu():
    #==Acciones para realizar por el usuario==#
    pass


# === Variables globales === #
baby=["Teletchi"]

child=[["Mizutamatchi","Tamatchi"],
       ["Mohitamatchi","Kuchitamatchi"]]

teen = [["Young Mametchi", "Batabatchi","Obotchi",["Nikatchi","Pirorirotchi"]],
        ["Hinatchi","Young Mimitchi","Hikotchi",["Hinotamatchi","Hashitamatchi"]]]

adult= [["Mametchi","Violetchi","Pyonkotchi"],["Kuchipatchi","Billotchi","Memetchi"],["Tarakotchi","Paparatchi","Mimiyoritchi"],["Tsunotchi","Hashizoutchi","Hanatchi"],["Megatchi","Masktchi","Kurokotchi"]
        ["ChoMamtechi","Decotchi","Mimitchi"],["Bunbuntchi","Debatchi","Hidatchi"],["Dorotchi","Pipotch","Bill"],["Androtchi","Teketchi","Wooltchi"],["Gozarutchi","Sekitoritchi","Warusotchi"]]

senior = ["Ojitchi","Otokitchi"]

genero = ["Macho", "Hembra"]

etapa = ["baby", "child", "teen", "adult", "senior"]

foods = {"apple":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "tart":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "pudding":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "cone":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "cereal":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "bread":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "sushi":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "scone":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "cheesecake":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 150}, 
        "apple pie":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 150}, 
        "cheese":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 100}, 
        "french fries":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 80}, 
        "milk":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 80}, 
        "steak":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 800}, 
        "turkey":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 600}, 
        "beef bowl":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 180}, 
        "BBQ":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 180}, 
        "sandwich":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 160}, 
        "grapes":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 160}, 
        "tacos":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 150},
        "hot dog":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 150},
        "cookie":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 150}, 
        "pizza":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 140}, 
        "pineapple":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 140}, 
        "corn dog":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 100}, 
        "parfait":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 130}, 
        "cake":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 600},
        "yoghurt":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 550},
        "melon":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 500}, 
        "energy drink":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 130}, 
        "bananas":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 130}, 
        "icecream":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 120}, 
        "cupcake":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 120}, 
        "creamy cake":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 120}, 
        "muffin":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 0}, 
        "sausage":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 110}, 
        "donut":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 110}, 
        "noodles":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 100}, 
        "hambuger":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 180}, 
        "soda":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 120}, 
        "chocolate":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 150}, 
        "pasta":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 200}, 
        "omelet":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 200}, 
        "drumstick":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 200}, 
        "popcorn":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 90}, 
        "fish":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 90}, 
        "cherry":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 90}, 
        "juice":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 80}, 
        "corn":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 80}, 
        "pear":{"calorias": 0, "cantidad": 0, "felicidad": 0, "precio": 70}
         }

items = {"cuckoo clock":{"precio": 4000},
        "costume":{"precio": 2500},
        "building blocks":{"precio": 800},
        "rc car":{"precio": 1000},
        "rc toy":{"precio": 1500},
        "tv":{"precio": 2500},
        "action figure":{"precio": 1400},
        "gramophone":{"precio": 5000},
        "shoes":{"precio": 1900},
        "wings":{"precio": 1000},
        "drum":{"precio": 1600},
        "cap":{"precio": 700},
        "sunglasses":{"precio": 800},
        "weights":{"precio": 600},
        "wig":{"precio": 1000},
        "doll":{"precio": 1400},
        "roller skate":{"precio": 1800},
        "mirror":{"precio": 3000},
        "trumpet":{"precio": 1800},
        "music":{"precio": 1500},
        "throne":{"precio": 5500},
        "royal costume":{"precio": 30000},
        "bow tie":{"precio": 700},
        "bow":{"precio": 500},
        "umbrella":{"precio": 500},
        "boom box":{"precio": 1400},
        "ball":{"precio": 200},
        "shirt":{"precio": 1000}
        }

tempItems = {"shovel":{"precio": 80},
            "plant":{"precio": 50},
            "chest":{"precio": 200},
            "lamp":{"precio": 700},
            "love potion":{"precio": 3000},
            "hair gel":{"precio": 400},
            "stuffed animal":{"precio": 0},
            "pencil":{"precio": 110},
            "music disc":{"precio": 0},
            "make-up":{"precio": 80},
            "fishing pole":{"precio": 400},
            "darts":{"precio": 100}
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