import random
def eleccion_de_palabra():
    palabras = {1: ['rojo', 'verde', 'azul', 'amarillo', 'marron', 'gris', 'negro', 'naranja'],
                2: ['perro', 'gato', 'lobo', 'tigre', 'leon', 'conejo', 'toro', 'liebre'],
                3: ['teclado', 'monitor', 'mouse', 'parlante', 'procesador', 'cooler']}
    print('(1)Para jugar con colores (2)Para jugar con animales (3)Para jugar con componentes del Hardware del computador')
    op = int(input('Elija una opcion: '))
    #Elijo aleatoriamente una palabra del conjunto seleccionado
    pal = palabras[op][random.randrange(len(palabras[op]))]
    return pal
#Estructura del ahorcado
def estructura_ahorcado():
    ahorcado = [' O ', '/|\\','/ \\']
    return ahorcado
#Estructura de la palabra
def estructura_de_la_palabra(pal):
    pal_est = []
    for y in pal:
        pal_est.append(['_ '])
    return pal_est
#Desarrollo del juego
def desarrollo_del_juego(pal,pal_est):
    letras_adivinadas = 0
    cuerpo = 0
    sigue = True
    #Mostrar en pantalla cantidad de letras de la palabra
    print('- ' * len(pal))
    while sigue:
        letra=input('Ingrese una letra: '.lower())
        if letra in pal:
            for pos in range(len(pal)):
                if(pal[pos]==letra):
                    pal_est[pos] = letra
                    letras_adivinadas = letras_adivinadas +1
            pal_imprimir =''
            for i in pal_est:
                pal_imprimir = pal_imprimir + i[0]
            print(pal_imprimir)
            if letras_adivinadas == len(pal):
                print('GANASTE')
                sigue=False
        else:
            cuerpo = cuerpo +1
            for y in range(cuerpo):
                print(estructura_ahorcado()[y])
            if (cuerpo == 3):
                print('PERDISTE')
                print('La palabra era: ', pal)
                sigue = False
#PROGRAMA PRINCIPAL
eleccion = 's'
while eleccion == 's'or eleccion =='si':
    pal = eleccion_de_palabra()
    desarrollo_del_juego(pal,estructura_de_la_palabra(pal))
    eleccion = str(input('Quiere seguir jugando? s/n').lower())
