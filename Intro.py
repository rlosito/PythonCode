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






