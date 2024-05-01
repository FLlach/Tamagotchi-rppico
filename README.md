# Tamagotchi rppico
 Creating a tamagotchi using Python and MicroPython for integration with a Raspberry Pi Pico

## Bibliography/Bibliografía :
[Tamagotchi Wiki] [text](https://tamagotchi.fandom.com/)
[MicroPython Documentation] [text](http://docs.micropython.org/en/latest/index.html)
[Raspberry Pi Pico Getting Started Guide] [text](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
[Raspberry Pi Pico Datasheet] [text](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)


## Utility/Utilidad
Healthy weight for each stage/Peso sano para cada etapa:
    Baby/bebé: Between 10 & 15 kg/Entre 10 y 15 kg
    Child/Niño: Between 15 & 30 kg/Entre 15 y 30 kg
    Teen/Adolescente: Between 30 & 40 kg/Entre 30 y 40 kg
    Adult/Adulto: Between 40 & 5 kg/Entre 40 y 55 kg
    Senior/Anciano: Between 40 & 55 kg/Entre 40 y 55 kg


## Functions/Funciones
-cambioHora: Asigns an initial time to the system/Asigna una hora inicial al sistema
reloj: Receives a list with 3 values (hour, minutes and seconds) and starts a chronometer modifying the values of the list/Recibe una lista con 3 valores (horas, minutos, segundos) e inicia un cronometro modificando los valores de la lista 

-petsPref: Modifies certain values on the favorites food based on the preferences of the virtual pet/Modifica ciertos valores de las comidas preferidas por los diferentes tipos de mascotas digitales 

-cambioFecha: Asigns an initial date to the system/Asigna una fecha de inicio al sistema

-main: Main function where the main actions that the user can use execute/Función principal donde se ejecutan las principales acciones que puede usar el usuario

-menu: Deploys a menu with the actions that the user can do/Despliega un menu con las acciones que puede realizar el usuario

## ClassMethods/MétodosDeClase
### User:
    -nombrar: Asigns a name to the user/Asigna un nombre al usuario
    -edad_generacion: Adds one generation of virtual pets to the user/Agrega una generación de mascotas al usuario
    -agregar_puntos: Adds tamapoint to the user's balance/Agrega tamapuntos al balance del usuario

### Tamagotchi: 
    dormir: Put the pet to sleep during a determined amount of time/Duerme a la mascota durante un tiempo determinado
    jugar: Deploys a menu with game options/Despliega un menu con opciones de juegos
    nombrar: Asigns a name to the virtual pet/Asigna un nombre a la mascota virtual
    comer: Deploys a menu where the user can choose to give to the virtual pet/Despliega un menu para elegir el tipo de comida que se le dará a la mascota virtual
    mostrar_estado: /Despliega las estadisticas actuales de la mascota virtual
    cagar: Adds a poop to the screen/Añade una caca a la pantalla
    limpiar: Clean the poop from the screen/Limpia la caca de la pantalla
        


## Trello
[Project Board] [text](https://trello.com/b/bw25POA6/tamagotchi-rppico)