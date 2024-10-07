
print('BOOLEANS:')

verdadero = True
falso = False

print(f'{verdadero} es de tipo {type(verdadero)}')
print(f'{falso} es de tipo {type(falso)}')


print('NEGANDO VALORES CON NOT:')

verdadero = True
falso = False

verdadero = not verdadero    #Ahora es False
verdadero = not True         #Ahora es False


falso = not falso            #Ahora es True
falso = not False            #Ahora es True


print(f'verdadero es {verdadero}')
print(f'falso es {falso}')
print(f'verdadero ahora es {not verdadero}')
print(f'falso ahora es {not falso}')


print('COMPARANDO VALORES:')

print(10 > 9)        #True
print(10 == 9)       #False
print(10 < 9)        #False

a = 200
b = 33

print('=> A es Mayor que B: ', a > b)      #True
print('=> B no es Mayor que A: ', b > a)   #False

print('EJECUTANDO CONDICIÓN:')

a = 200
b = 33


if b > a:
  print("b es mayor que a")
else:
  print("a es mayor que b")


print('EVALUANDO VALORES CON LA FUNCIÓN BOOL')

x = 12
name = 'luis'

print(f'{x} es {bool(x)}')          #True
print(f'{name} es {bool(name)}')    #True  
print(bool(23))                     #True
print(bool(0))                      #False
print(bool('Hello'))                #True
print(bool(''))                     #False
print(bool(None))                   #False


print('FUNCIONES CON VALORES BOOLEANOS:')

def myFunction():
  return True

print(myFunction())

if myFunction():
  print('Yes')
else:
  print('NO!')


print('USANDO ISINSTANCE')

x = 200

print(isinstance(x, int))   #Consulta si x es un int, imprime True
print(isinstance(x, str))   #False