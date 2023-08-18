print("hola mundo")

# capitulo 2 python. 

"""

Comentario 
multi linea 

"""

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


