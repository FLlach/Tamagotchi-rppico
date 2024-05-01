# Tamagotchi rppico
 Creating a tamagotchi using Python and MicroPython for integration with a Raspberry Pi Pico

## Bibliography/Bibliografía :
[Tamagotchi Wiki](https://tamagotchi.fandom.com/)
[MicroPython Documentation](http://docs.micropython.org/en/latest/index.html)
[Raspberry Pi Pico Getting Started Guide](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
[Raspberry Pi Pico Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)


## Utility/Utilidad
Healthy weight for each stage/Peso sano para cada etapa:
- Baby/bebé: Between 10 & 15 kg/Entre 10 y 15 kg
- Child/Niño: Between 15 & 30 kg/Entre 15 y 30 kg
- Teen/Adolescente: Between 30 & 40 kg/Entre 30 y 40 kg
- Adult/Adulto: Between 40 & 5 kg/Entre 40 y 55 kg
- Senior/Anciano: Between 40 & 55 kg/Entre 40 y 55 kg


## Functions/Funciones
- `cambioHora`:
&nbsp;&nbsp;&nbsp;&nbsp;Asigns an initial time to the system
&nbsp;&nbsp;&nbsp;&nbsp;Asigna una hora inicial al sistema
- `reloj`: 
&nbsp;&nbsp;&nbsp;&nbsp;Receives a list with 3 values (hour, minutes and seconds) and starts a &nbsp;&nbsp;&nbsp;&nbsp;chronometer modifying the values of the list
&nbsp;&nbsp;&nbsp;&nbsp;Recibe una lista con 3 valores (horas, minutos, segundos) e inicia un cronometro &nbsp;&nbsp;&nbsp;&nbsp;modificando los valores de la lista 

- `petsPref`: 
&nbsp;&nbsp;&nbsp;&nbsp;Modifies certain values on the favorites food based on the preferences of the virtual pet
&nbsp;&nbsp;&nbsp;&nbsp;Modifica ciertos valores de las comidas preferidas por los diferentes tipos de mascotas digitales 

- `cambioFecha`: 
&nbsp;&nbsp;&nbsp;&nbsp;Asigns an initial date to the system
&nbsp;&nbsp;&nbsp;&nbsp;Asigna una fecha de inicio al sistema

- `main`: 
&nbsp;&nbsp;&nbsp;&nbsp;Main function where the main actions that the user can use execute
&nbsp;&nbsp;&nbsp;&nbsp;Función principal donde se ejecutan las principales acciones que puede usar el usuario

- `menu`: 
&nbsp;&nbsp;&nbsp;&nbsp;Deploys a menu with the actions that the user can do
&nbsp;&nbsp;&nbsp;&nbsp;Despliega un menu con las acciones que puede realizar el usuario

## ClassMethods/MétodosDeClase
### User:
- `nombrar`: 
&nbsp;&nbsp;&nbsp;&nbsp;Asigns a name to the user
&nbsp;&nbsp;&nbsp;&nbsp;Asigna un nombre al usuario
- `edad_generacion`: 
&nbsp;&nbsp;&nbsp;&nbsp;Adds one generation of virtual pets to the user
&nbsp;&nbsp;&nbsp;&nbsp;Agrega una generación de mascotas al usuario
- `agregar_puntos`: 
&nbsp;&nbsp;&nbsp;&nbsp;Adds tamapoint to the user's balance
&nbsp;&nbsp;&nbsp;&nbsp;Agrega tamapuntos al balance del usuario

### Tamagotchi: 
- `dormir`: 
&nbsp;&nbsp;&nbsp;&nbsp;Put the pet to sleep during a determined amount of time
&nbsp;&nbsp;&nbsp;&nbsp;Duerme a la mascota durante un tiempo determinado
- `jugar`: 
&nbsp;&nbsp;&nbsp;&nbsp;Deploys a menu with game options
&nbsp;&nbsp;&nbsp;&nbsp;Despliega un menu con opciones de juegos
- `nombrar`: 
&nbsp;&nbsp;&nbsp;&nbsp;Asigns a name to the virtual pet
&nbsp;&nbsp;&nbsp;&nbsp;Asigna un nombre a la mascota virtual
- `comer`: 
&nbsp;&nbsp;&nbsp;&nbsp;Deploys a menu where the user can choose to give to the virtual pet
&nbsp;&nbsp;&nbsp;&nbsp;Despliega un menu para elegir el tipo de comida que se le dará a la mascota virtual
- `mostrar_estado`: 
&nbsp;&nbsp;&nbsp;&nbsp;Deploys the actual stats of the virtual pet
&nbsp;&nbsp;&nbsp;&nbsp;Despliega las estadisticas actuales de la mascota virtual
- `cagar`: 
&nbsp;&nbsp;&nbsp;&nbsp;Adds a poop to the screen
&nbsp;&nbsp;&nbsp;&nbsp;Añade una caca a la pantalla
- `limpiar`: 
&nbsp;&nbsp;&nbsp;&nbsp;Clean the poop from the screen
&nbsp;&nbsp;&nbsp;&nbsp;Limpia la caca de la pantalla
        


## Trello
[Project Board](https://trello.com/b/bw25POA6/tamagotchi-rppico)