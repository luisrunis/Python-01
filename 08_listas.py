

print('CREANDO LISTAS:')

lista1 = ['uno', 'dos', 'tres', 'uno']
lista2 = [1,2,3,4,5,1]
lista3 = [True, False, True]
lista4 = ['uno', 2, True]

print('lista1 => ', lista1, type(lista1), len(lista1))
print('lista2 => ', lista2, type(lista2), len(lista2))
print('lista3 => ', lista3, type(lista3), len(lista3))
print('lista4 => ', lista4, type(lista4), len(lista4))


#**********************************
print('USANDO CONSTRUCTOR LIST():')

cadena = ''

lista5 = list(cadena)
print('lista5 => ', lista5, type(lista5), len(lista5))

cadena = 'Hola mundo'
lista6 = list(cadena)
print('lista6 => ', lista6, type(lista6), len(lista6))

tupla = ('uno', 2, False)
lista = list(tupla)
print('tupla => ', tupla, type(tupla), len(tupla))
print('lista => ', lista, type(lista), len(lista))


#******************
print('USANDO RANGE() PARA CREAR LISTA:')

lista7 = list(range(0,10))      #Imprime del 0 al 9
lista8 = list(range(1,20,2))    #Imprime desde el 1, con salto de 2 hasta el 19
lista9 = list(range(10,0,-1))   #Imprime desde el final, desde el 10 hasta el 1

print('lista7 => ', lista7, type(lista7), len(lista7))
print('lista8 => ', lista8, type(lista8), len(lista8))
print('lista9 => ', lista9, type(lista9), len(lista9))



#**************************
print('DESEMPAQUETANDO LISTAS:')

lista = ['uno', 'dos', 'tres']

print('lista => ', lista)

x,y,z = lista

print('x => ', x, type(x))
print('y => ', y, type(y))
print('z => ', z, type(z))


print('=' * 20)

lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
[a, b, *c] = lista
print('a => ', a)
print('b => ', b)
print('c => ', c)

print('=' * 20)

lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
[a, *b, c] = lista
print('a => ', a)      
print('b => ', b)      
print('c => ', c)


#**************************
print('ACCEDIENDO A LOS VALORES DE LA LISTA:')

lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']

print(lista[2])       #tres
print(lista[-1])      #seis
print(lista[2:5])     #Imprime los valores desde la posición 2 hasta la 4
print(lista[:4])      #Imprime desde el inicio hasta la posición 3
print(lista[2:])      #Improme desde la posición 2 hasta el final
print(lista[-4:-1])   #Imprime contando desde el final en la posición -4 hasta -1



#*************************
print('COMPROBAR VALORES EN LISTA')

lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']

if 'tres' in lista:
    print('valor encontrado')
else:
    print('valor no encontrado')

print('tres' in lista)    #True
print('siete' in lista)   #False



#**********************
print('CAMBIANDO VALORES DE LISTA:')

lista = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(lista)

lista[0] = 'grape'
lista[2] = 'coco'
print(lista)

print('=' * 20)


#***********************
print('RECORRER LISTA USANDO FOR:')

lista = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

for x in lista:
    print(x)


print('USANDO RANGE')

for i in range(len(lista)):
    print(lista[i])


print('USANDO WHILE')

i = 0
while i < len(lista):
    print(lista[i])
    i = i+1


print('USANDO COMPREHENSIONS:')

lista = ["apple", "banana", "cherry"]

print('= Forma Normal = ')

for x in lista: 
  print(x)


print('= Comprehensions1 = ')

lista = [x for x in lista]
print(lista)


print('= Comprehensions2 = ')

lista = [print(x) for x in lista]

