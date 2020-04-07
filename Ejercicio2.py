tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
lista =[]
for i in tam:
    name, espace, tupla = i.partition(' ')
    x,y = tupla.split(',')
    lista.extend([(x,y)])
lista.sort()
print(lista)
