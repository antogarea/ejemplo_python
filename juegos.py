import hangman
import reversegam
import tictactoeModificado
import json
        #• Definir y justificar la estructura de datos a utilizar:
#  La estructura elegida para el manejo de la informacion es un diccionario:
# con clave 'jugadores',donde el valor de esta es una lista(donde se va a almacenar un diccionario por cada jugador)
# me parecio mas sencilla esta estructura para poder cargar a los jugadores solo con un append().
        #• Elegir y justificar el formato de archivo a utilizar:
#  Elegi el formato json por tener mas legibilidad que pickle,en el sentido de que me permitió ir abriendo el archivo
# en un editor de texto e ir verificando los datos que el programa almacenaba y así poder ir corrigiendo errores.

def mostrarContenido(data):
        for jugador in data['Jugadores']:
            print('Nombre: ', jugador['Nombre'])
            print('Jugó al: ', jugador['Juego'])
            print('')

def escriboJson(data):
    # Escribo en el archivo
    with open('Jugadores.json','w') as file:
        # Como en data tengo toda la informacion(vieja y actual)
        # Abro el archivo con 'w' y sobrescribo el contenido
        json.dump(data,file,indent=4)

def cargarJson(dict,juego):
    #Agrego un nuevo jugador a mi lista
    nom=input(str('Ingrese su nombre:'))
    #Por cada jugador tengo un diccionario con su nombre y opcion de juego
    dict['Jugadores'].append({
        'Nombre': nom,
        'Juego': juego})

def cargarInfo():
    try: #SI EXISTE EL ARCHIVO
        with open('Jugadores.json') as file:
            #retorno el contenido el archivo
            return json.load(file)
    except: #SI NO EXISTE, LO CREO
        print('El archivo no existe, se va a crear')
        with open('Jugadores.json','w') as file:
            return {'Jugadores':[]}

def main(args):
    sigo_jugando = True
    #Almaceno en data lo retornado por la funcion(un diccionario)
    data=cargarInfo()
    while sigo_jugando:
        print('''
		Elegí una opcion :
		1.- AHORCADO
		2.- Ta-TE-TI
		3.- REVERSE
		4.- Salir del menu o mostrar jugadores ''')
        opcion = input()
        if opcion == '1':
            juego = 'AHORCADO'
            # Agrega un jugador en el archivo
            cargarJson(data,juego)
            hangman.main()
        elif opcion == '2':
            juego='TA-TE-TI'
            # Agrega un jugador en el archivo
            cargarJson(data, juego)
            tictactoeModificado.main()
        elif opcion == '3':
            juego='REVERSE'
            # Agrega un jugador en el archivo
            cargarJson(data, juego)
            reversegam.main()
        elif opcion == '4':
            print('Quiere ver el listado de los usuarios que jugaron? si/no')
            op=input().lower()
            if op=='si' or op=='s':
                mostrarContenido(data)
            #Escribo en el json
            escriboJson(data)
            sigo_jugando = False

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

