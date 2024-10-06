
print('NÚMEROS:')

x = 2
y = 3.5
z = 4j

print(f'{x} es de tipo {type(x)}')
print(f'{y} es de tipo {type(y)}')
print(f'{z} es de tipo {type(z)}')


print('NÚMEROS ENTEROS:')

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


print('NÚMEROS FLOTANTES:')

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


print('CONVERSÓN DE NÚMEROS:')

x = float(1)                                    #1.0


y = int(2.8)                                    #2


z = complex(1)                                  #1j

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


print('NÚMEROS ALEATOREOS:')

import random

print('Número aleatoreo de 0 a 9 => ', random.randrange(1,10))


numeros = [1,2,3,4,5,6,7,8,9]
print('numeros => ', numeros)
print('numero aleatoreo de la lista => ', random.choice(numeros))