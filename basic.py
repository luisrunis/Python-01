#Comentario de una sola linea


'''
Comentario 
de 
varias 
linea
'''

#*****************
#*VARIABLES
nombre = 'luis'
apellido = 'runiz'
edad = 30

print('nombre:' + nombre)
print('apellido:' + apellido)
print(f'edad: {edad}')


print('=' * 20)
#************************


x,y,z = 'uno', 'dos', 'tres'

print(f'x: {x}')
print(f'y: {y}')
print(f'z: {z}')


print('=' * 20)
#************************

x = y = z = 'Orange'

print(f'x: {x}')
print(f'y: {y}')
print(f'z: {z}')


print('=' * 20)
#************************

print('Variable de alcance global')

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


print('=' * 20)
#************************

print('Variable de alcance local')


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)


myfunc()
print("Python is " + x)


print('=' * 20)
#************************

print('Palabra clace global')
#*La palabra clave global hace que la variable dentro una función sea global.

def myfunc():
  global x
  x = 'fantastic'


myfunc()
print('Python is ' + x)