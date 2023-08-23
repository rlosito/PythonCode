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

"""LetraEncontrada = False
letra = "a"
frase = "En este momento estoy buscando la letra a"
indice = 0

while( not(LetraEncontrada)):
    if(frase[indice] == letra):
        LetraEncontrada = True
    else:
        indice += 1

print (f"letra encontrada en posicion : {indice} ")"""

# Funciones reservadas de los bucles 
# Break    --> parada para abandonar el bucle
# Continue --> Saltamos a la siguiente iteracion del bucle
"""letra = "a"
frase = "buscando la letra a"
count = 0

for caracter in frase:
    if (caracter == letra):
        count +=1
        print (f"- Letra Encontrada {count} veces.")
        continue
    print("No hemos encontrado nada.")"""


# Pass     --> No hace nada con la iteracion (ni sale de la iteracion y tampoco sale del bucle)
# solo se utiliza para dejar vacio una parte del codigo a la espera de ser completado. 

def funciondeejemplo (Arg1,Arg2):
    pass 
    # en python no podriamos dejar vacia la definicion de una funcion.
    # pero con esta instruccion podemos hacerlo y dejar la funcion definida pero sin codigo. 

# Else    --> Se utiliza para ejecutar algo cuando termine el bucle, pero si por alguna
# razon finaliza el bucle antes de su ultima iteracion, ya esta parte no se ejecuta 

"""frase = "contando numero de caracteres de una frase"
count = 0
for caracter in frase:
    count += 1
    if (caracter == "l"): # si la frase contiene un caracter "l", salimos del bucle y no mostramos el contador
        break
else: # si el bucle termina todas las iteraciones entonces ejecutara esta parte. 
    print(f"La frase tiene {count} caracteres")
"""    

# Listas

""" 
- Recordatorio para definir una lista 
NomLista = [1,2,"hola",True]  # pueden tener elementos de todos los tipos, numericos, texto, booleanos y objetos. 

- para acceder al contenido de la lista 
valor = NomLista[0] --> en numero es el numero del elemento de la lista, empiezan en el cero. 

- para obtener el numero de elementos de una lista 
longitud = len(NomLista)

- iterar en los elementos de una lista
for num in NomLista:
    print(num)

# Indexado de las listas. 
lista = ["dale","un","buen","like","crack"]
ultimaposicion = lista[-1] # con los indices negatios podemos acceder desde el final a una lista ej: -1 al ultimo elemento, -2 al penultimo elemento, -3 al antepenultimo, etc
penultimaposicion = lista[-2]

# Sublistas 
# cuando quieres obtener varios valores de una lista a la vez 
# Hay que definir el limite inferior (En este caso 1 representa el segundo valor) y el limite superior (En este caso el 4 representa el tercer valor de la lista) recordar que la lista al empezar a contrar por cero hay que restar -1 para obtener que posicion es realmente
Sublista = lista[1:4]  # ej: si imprimimos el resultado seria ["un","buen","like"]

# con las sublistas podemos ir desde el comienzo de la lista hasta cierto elemento o al reves
Sublista = lista[:4]  # desde el comienzo hasta el elmento numero 3 ["dale","un","buen","like"]
Sublista = lista[2:]  # Desde el tercer elemento hasta el final     ["buen","like","crack"]

# con las sublistas tambien se pueden utilizar indices negativos.
Sublista = lista[-4:-1] # ej ["un","buen","like"]
"""
# comprobar si una lista contine o no un elemento 
"""lista = ["dale","un","buen","like","crack"]
palabra = "like"
palabrados = "melocoton"

if (palabra in lista):
    print("La palabra pertenece a la lista")

if (palabrados not in lista):
    print("la palabra no esta en la lista")"""

# modificar elementos de uan lista 
"""
lenguajes = ["c","java","python","javascript","Kotlin"]
print(lenguajes)
lenguajes[1] = "angular"
print(lenguajes)
lenguajes[0] = lenguajes[0] + "++"
print(lenguajes)

lenguajes[2:4] = ["anaconda","typescript"]
print(lenguajes)"""

# caso especial podemos sustituir un valor por varios valores 
"""
lenguajes = ["c","java","python","javascript","Kotlin","ruby","Rust"]
print(lenguajes)
lenguajes[4:5] = ["varios","Valores","Botella"] # En la posicion del elemento "Kotlin" es sustituido por los tres elemtentos ["varios","Valores","Botella"]
print(lenguajes) # ['c', 'java', 'python', 'javascript', 'varios', 'Valores', 'Botella', 'ruby', 'Rust']
"""
# Metodos de las listas: Añadir elementos
# En Python podmeos utilizar metodos con las listas.
# Para ejecutar estos metodos: variableDeTipoLista.metodo()
"""
lenguajes = ["c","java","python","javascript","Kotlin","ruby","Rust"]
print(lenguajes)
lenguajes.insert(1,"C++")
print(lenguajes)

lenguajes.append("Typescript")
print(lenguajes)

lenguajesdos = ["Angular","Vue","React"]
lenguajes.extend(lenguajesdos)
print(lenguajes)
print(lenguajesdos)
"""
# Metodos de las listas: Eliminar  elementos
frutas = ["platano","kiwi","papaya","melocoton","cereza"]
print(frutas)

frutas.pop() # sin pasarle un indice, elimina el ultimo elemento de la lista
print(frutas)

elementoeliminado = frutas.pop(0) # con indice elimina el elemento señalado por el indice, en este caso el primero
print(frutas)
print(elementoeliminado) # como curiosidad el metodo pop retorna el elemento que elimina, por si lo queremos reutilizar. 

frutas.remove("kiwi")
print(frutas)

del frutas[0]
print(frutas)

# Metodo para buscar en las listas
frutas = ["platano","kiwi","papaya","melocoton","cereza"]
indice = frutas.index("melocoton")
print(indice)