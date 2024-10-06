
print('CADENA DE CARACTERES:')

a = "John"
b = 'John'
c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
d = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(type(a))   #<class 'str'>
print(type(b))   #<class 'str'>
print(type(c))   #<class 'str'>
print(type(d))   #<class 'str'>


print('LONGITUD DE LA CADENA')

x = 'Colombia'
print(len(x))


print('INDEXING:')

x = 'Colombia'
print(x)
print(x[0])      #C
print(x[1])      #0
print(x[-1])     #


print('RECORRER UNA CADENA:')

for i in 'banana':
    print(i)


print('=' * 20)

x = 'banana'

for i in x:
    print(i)


print('VERIFICAR CADENA:')

txt = "The best things in life are free!"
print("free" in txt)         #True
print('super' in txt)        #False


if 'best' in txt:
    print('yes, best está en el texto')


print('expansive' not in txt)     #True

if 'expansive' not in txt:
    print('yes, no está en el texto')



print('SLICING:')

x = 'Colombia'

print(x[2:5])       #Imprime desde posición 2 hasta la 4 = lom 
print(x[:5])        #Imprime desde la posición 0 hasta la 4  = Colom
print(x[2:])        #Imprime desde la posición 2 hasta el final = lombia
print(x[-5:-2])     #Imprime desde el final de la cadena en la posición 4 hasta el -2 = omb


print('CONCATENAR CADENAS:')

a = "Hello"
b = "World"
c = a + " " + b
print(c)


print('FORMATEAR CADENA:')

articulo = 'computador'
precio = 50
print(f'el valor del {articulo} es de {precio} dolares')

txt = f'el valor del {articulo} es de {precio * 2 } dolares'
print(txt)


print('METODOS DE CADENA:')

x = 'Hola mundo'
print(x.upper())
print(x.lower())
print(x.split())
print(x.replace('mundo', 'luis'))