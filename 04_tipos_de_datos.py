

#* TIPOS DE DATOS:

#* En Python, el tipo de datos se establece cuando asignas un valor a una variable:
#* Python tiene los siguientes tipos de datos integrados de forma predeterminada.


x = "Hello World"                                              #str
x = 20                                                         #int
x = 20.5                                                       #float
x = 2j                                                         #complex
x = True                                                       #bool
x = b"Hello"                                                   #bytes
x = bytearray(5)                                               #bytearray
x = memoryview(bytes(5))                                       #memoryview
x = None                                                       #NoneType
x = ["apple", "banana", "cherry"]                              #list
x = ("apple", "banana", "cherry")                              #tuple
x = {"apple", "banana", "cherry"}                              #set
x = {"name" : "John", "age" : 36}                              #dict
x = frozenset({"apple", "banana", "cherry"})                   #frozenset


#* CONVERSIÓN IMPLÍCITA: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos: 

a = 10          #int
b = 2.5         #float
c = a + b       #int + float = float


print(type(a))
print(type(b))
print(type(c))

print(f' {a} es de tipo {type(a)}')
print(f' {b} es de tipo {type(b)}')
print(f' {c} es de tipo {type(c)}')



#* CONVERSIÓN EXPLÍCITA: Es realizada por nosotros. Si desea especificar el tipo de dato, puede realizar la conversión mediante las siguientes funciones constructoras:

x = str(3)    
x = int(3.5)    
x = float(3)
x = complex(5)
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))
x = list(("apple", "banana", "cherry"))
x = tuple(["apple", "banana", "cherry"])
x = set(("apple", "banana", "cherry"))
x = dict(name="John", age=36)
x = frozenset(("apple", "banana", "cherry"))

