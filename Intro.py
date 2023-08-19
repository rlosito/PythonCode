print("hola mundo")

# capitulo 2 python. 

"""

Comentario 
multi linea 

# ejercicio 

Txt = input("Introduce un numero :")  # todo el texto que se pilla por el imput siempre es String

if (Txt.isnumeric()): # .isnumeric solo esta en las var string
    Txt = int(Txt)
    # verificar si es par o impar
    if( Txt%2 == 0 ):
        print("Es numero par")
    else:
        print("Es numero impar")
else:
    print("No es un numero")


# funciones de python

def Saludar():
    print("primera funcion")

# para usar la funcion
Saludar()
    

# Funcion con argumentos
def saludardos(nombre):
    print("hola " + nombre + " que tal?")

saludardos("Pepe")
saludardos("M.Rajoy")

# Funcion con retorno
def suma(a,b):
    resultado = a + b 
    return resultado

valor = suma(10,5)
print(valor)

# funcion con valor por defecto 
def Saludarpordefecto(nombre="Loso"):
    print("Hola " + nombre + "que tal ?")

Saludarpordefecto() # utilizara el valor por defecto
Saludarpordefecto("Pepe") # utilizara el valor pepe

# funcion que retorna varios valores
def sumayresta(a,b):
    suma = a + b 
    resta = a - b 
    return suma, resta

resultado1, resultado2 = sumayresta(10,5)
print("Los resultado son:\nSunma:" + str(resultado1) + "\nResta:" + str(resultado2))

# Ejercicio 1 de funciones 
def Esnumero (num):
    if (type(num)==int):
        return True
    else:
        return False

def SacarMaximo (Num1, Num2):
    # comprobar que numero es el mayor
    if (Num1 > Num2):
       print ("Numero " + str(Num1) + " es mayor que " + str(Num2))
    elif (Num1 == Num2):
       print ("Ambos numeros son iguales") 
    else:
       print ("Numero " + str(Num2) + " es mayor que " + str(Num1))

Num1 = 55
Num2 = 3

if (Esnumero(Num1) and Esnumero(Num2)):
    SacarMaximo (Num1,Num2)
else:
    print("una de las variables no es un numero")



# -Introduccion a la lista.
numeros = [1,2,3,4,5]  # como las tablas la primera posicion del indice es la cero. 
# para acceder a un elemento de la lista 
numeros[0] # hace referencia al primer elemento de la lista llamada numeros.
len(numeros) # para obtener el numero de elementos de la lista.

# Bucles for
for x in range(5):  # con solo un argumento indica que empieza en 0 y llega hasta 4 (son 5 iteraciones) 0,1,2,3,4
    print(x)

for x in range(5,10):  # con dos argumentos indica limite superior e infierior: empiez en el 5 y termina en el 9 --> 5,6,7,8,9
    print(x)

for x in range(5,20,2):  # con tres argumentos indica limite superior e infierior y el incremento: empieza en el 5 y termina en el 19 --> 5,7,9,11,13,15,17,19
    print(x)

for x in range(5,21,2):  # empieza 5,7,9,11,13,15,17,19 como el limite es el valor superior -1 (21 en este caso) no es alcanzable la ultima iteracion no se hace. 
    print(x)

# mini ejemplo, sacar las vocales de una palabra:
palabra = "hola"
for letra in palabra:
    if (letra == "a" or letra == "e" or letra=="i"or letra=="o"or letra=="u"):
        print(letra)
    else:
        print("Es una consonante")
""" 

# mini ejemplo, trabajar con lista dentro del bucle. 
"""numeros = [1,2,3,4,5]
for numero in numeros:
    print(numero)
    numero += 10
    print(numero)"""

"""print(numeros)"""
# conclusion no hemos modificado el valor de la lista 

"""for indice in range(len(numeros)):
    numeros[indice] += 10
print(numeros)"""
# conclusion aqui si hemos cambiado los valores de la lista 


# BUCLE WHILE
"""cont = 0
while(cont < 10):
    print(cont)
    cont += 1"""

LetraEncontrada = False
letra = "a"
frase = "En este momento estoy buscando la letra a"
indice = 0

while( not(LetraEncontrada)):
    if(frase[indice] == letra):
        LetraEncontrada = True
    else:
        indice += 1

print (f"letra encontrada en posicion : {indice} ")



