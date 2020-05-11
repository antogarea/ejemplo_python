import hangman
import reversegam
import tictactoeModificado
import json

def cargarJson(dict,juego):
    nom=input(str('Ingrese su nombre:'))
    dict['Jugadores'].append({
        'Nombre': nom,
        'Juego': juego})

def cargarInfo():
    try:
        with open('Prueba5.json') as file:
            return json.load(file)
    except:
        with open('Prueba5.json','w') as file:
            return {'Jugadores':[]}

def main(args):
    sigo_jugando = True
    data=cargarInfo()
    while sigo_jugando:
        print('''
		Elegí con qué juego querés jugar:
		1.- AHORCADO
		2.- Ta-TE-TI
		3.- REVERSE
		4.- Salir del menu o mostrar jugadores anteriores''')
        opcion = input()
        if (opcion != '4'):
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
        if (opcion == '4'):
            print('Quiere ver el listado de usuarios que jugaron? si/no')
            op=input().lower()
            if op=='si' or op=='s':
                for jugador in data['Jugadores']:
                    print('Nombre: ', jugador['Nombre'])
                    print('Jugó al: ', jugador['Juego'])
                    print('')
            with open('Prueba5.json','w') as file:
                json.dump(data,file,indent=4)
            sigo_jugando = False

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

