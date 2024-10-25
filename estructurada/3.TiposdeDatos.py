from xmlrpc.client import boolean

from unicodedata import decimal

if __name__== '__main__':
entero = 42                         #int
decimal = 3.14                      #float
complejo = 2+3j                     #complex
booleano = True                     #bool
cadena = "hola, phyton!"            #str
binario = bytes([50,100,150])      #bytes


print("tipos basicos:")
print("entero:",entero)
print("decimal:",decimal)
print("complejo:",complejo)
print("booleano:",booleano)
print("cadena:",cadena)
print("binario: ", binario,"\n")


# estructura de datos avanzada
lista = [1,2,3,"cuatro"] # list
tupla = [5,6,7, "ocho"]     #tuple
conjunto =[9,10, "once", "doce"] #set
diccionario = {"clave1": "valor1","clave2": 28}
print("estructuras avazadas:")
print("lista:", lista)
print("tupla:", tupla)
print("conjunto:", conjunto)
print("diccionario:", diccionario, "\n")

#otros tipos especiales
nulo = None     # nonetype
rango = range(3) # range (equivale a [0,

print("tipos especiales:")
print("nulo", nulo)
print("rngo:", list(rango)) #convertimos a listaa

# ejemplo de iteracion con el tipo range
print ("\nIterando sobre el rango:")
for numero in rango:
    print (numero)
