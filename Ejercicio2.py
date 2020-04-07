tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
lista =[]
for i in tam:
    name, espace, tupla = i.partition(' ')
    x = int(tupla.split(',')[0])
    y = int(tupla.split(',')[1])
    lista.extend(([(x,y)]))
lista.sort()
print(lista)
#No me fue posible utilizar la funcion sort() sin pasar los parametros a enteros
#Lo probe de mil maneras y solo me funciona de esta manera
#Por ejemplo, de esta forma no me funciona:
    #tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
    #lista =[]
    #for i in tam:
    #    name, espace, tupla = i.partition(' ')
    #    x,y = tupla.split(',')
    #    lista.extend([(x,y)])
    #lista.sort()
    #print(lista)
