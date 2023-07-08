from random import choice 

#variables que se van a utilizar para todas las funciones
palabras = ['casa','avion','matematicas']
letras_incorrectas = [] 
letras_correctas = [] 
intentos = 5 
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    '''
    Esta función tomará de lista_palabras para elegir
    una palabra de forma aleatoria, esta será la palabra
    que el jugador deverá adivinar. 
    '''
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

palabra = elegir_palabra(palabras)

def mostrar_nuevo_tablero(palabra_elegida):
    '''
    Esta función toma la palabra_elegida que el jugador debe adivinar.
    Y se encarga de pintar lo que aparecerá por pantalla.
    Por cada letra de palabra_elegida voy a revisar si ya fue descubierta
    ,en caso que así lo sea muestro la letra , caso contrario muestro un guion.
    '''

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(lista_oculta)

palabra_elegida, letras_unicas = elegir_palabra(palabras)

# while not juego_terminado:
#     pass 