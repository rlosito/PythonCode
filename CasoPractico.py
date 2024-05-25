#=======================================================
# Synopsis
#   Title : Caso practico curso de Pyton 
#   Author: Rafael.losito@globaltms.com
#   Date  : 22/05/2024    

# DESCRIPTION
#   Programa de creacion modificacion y borrado de tareas. 

#NOTES
#   

#COMPONENT
#   

#=======================================================

# =========
# inicio
# =========
# Imports 
import os

# variables gloables
Indice = 1
DicTarjetas = {}

# =========
# clases
# =========
class Tarjeta:

# Constructor
    def __init__ (self, Indice, Titulo, Contenido):
        self.Indice    = Indice
        self.Titulo    = Titulo
        self.Contenido = Contenido
        self.__Estado    = "Pendiente"

# Metodo, retorna si la tarea es pendiente o no
    def EstaPendiente(self):             
        if self.__Estado == "Pendiente":
           return True
        else:
           return False

# Metodo, cambia la fecha de la tarea 
    def UpdateTarea(self):             
        if self.__Estado == "Completada":
           self.__Estado = "Pendiente"
        else:
           self.__Estado = "Completada"


# =========
# funciones
# =========

# funcion de agregar tareas al diccionario1
def pantalla_crearTarea(Indice):
    os.system("Cls")    
    print ("===============================")
    print ("         NUEVA TAREA           ")
    print ("===============================")
    print ("")    
    tmptitulo    = input ("Titulo.....:")
    tmpContenido = input ("Contenido..:")
    
    Repetir = True
    while Repetir:
        print ("")    
        Resp = input ("Los datos son correctos (S/N) .:")
        if Resp == "S" or Resp == "s":
           # Añádimos la tarea al diccionario
           NewTarjeta = Tarjeta(str(Indice),tmptitulo,tmpContenido)
           DicTarjetas[str(Indice)] = NewTarjeta
           Indice = Indice + 1

           # Salimos de la pantalla guardar 
           Repetir = False
           print ("Datos guardados")
           Resp = input ("Pulse enter para continuar .:")

        elif Resp == "N" or Resp == "n":
            # salimos de la pantalla guardar sin añadir la tarea
            Repetir = False
            print ("Datos no guardados")    
            Resp = input ("Pulse enter para continuar .:")

        else:
            # pedimos la introduccion de opcion correcta
            print ("Respuesta erronea, seleccione una de las dos opciones.")    

    return Indice

# Funcion que listara las creadas y su estado 
def Listar_Tareas(DicTarjetas):
    for key in DicTarjetas:

        print ("Indice : [ " + DicTarjetas[key].Indice + " ] " ,end="")
        print ("Titulo : [ " + DicTarjetas[key].Titulo + " ] ",end="")
        print ("Contenido : [ " + DicTarjetas[key].Contenido + " ] ",end="")
        if DicTarjetas[key].EstaPendiente():
           print (" Estado : [ Pendiente ]")
        else:
           print (" Estado : [ Completada ]")

# Funcion para la pantalla de solo listar tareas
def Pantall_Listar_Tareas (DicTarjetas):
    os.system("Cls")
    print("==================================")
    print("      Listado de tareas")
    print("==================================")    
    print()

    Listar_Tareas(DicTarjetas)

    print()

    Resp = input ("Pulse enter para continuar .:")

# funcion para cambiar el estado de las tareas. de pendiente --> completada y de completada --> pendiente
def Pantalla_Cambio_Estado(DicTarjetas):
    os.system("Cls")
    print("==================================")
    print("    Cambio de estado de tareas ")
    print("==================================")    
    print()

    Listar_Tareas(DicTarjetas)

    print()    

    # Introducimos el indice de la tarea a modificar el estado. 
    tarea_Seleccion = input("Indique el indice de la tarea que quiere cambiar el estado .:")

    if tarea_Seleccion in DicTarjetas:
        # La tarea existe por lo que se pude cambiar de estado
        if DicTarjetas[tarea_Seleccion].EstaPendiente():
            print("La tarea esta PENDIENTE y se cambiara a COMPLETADA")
            
        else:
            print("La tarea esta COMPLETADA y cambiara a PENDIENTE")
        
        resp = input("Desea proceder (S/N) .:")
        if resp == "S" or resp == "s":
           # grambamos el cambio en la tarea 
           objtemp = DicTarjetas[tarea_Seleccion]
           objtemp.UpdateTarea()
           DicTarjetas[tarea_Seleccion] = objtemp
           print("Cambio completado")        
           temresp = input ("Pulse enter para continuar")
        else:
           # anulamos el cambio en la tarea
           print("Cambio anulado")        
           temresp = input ("Pulse enter para continuar")            
    else:
        # La Tarea seleccionada no existe 
        print("La tarea que esta intenando seleccionar no existe")        
        temresp = input ("Pulse enter para continuar")

# funcion para seleecionar una taraa y borrarla 
def Pantalla_Borrado_Tarea(DicTarjetas):
    os.system("Cls")
    print("==================================")
    print("       Borrado de Tarea  ")
    print("==================================")    
    print()

    Listar_Tareas(DicTarjetas)

    print()    

    # Introducimos el indice de la tarea a modificar el estado. 
    tarea_Seleccion = input("Indique el indice de la tarea que quiere borrar .:")

    if tarea_Seleccion in DicTarjetas:
        # La tarea existe por lo que se puede intentar borrar 
        resp = input("Desea proceder (S/N) .:")
        if resp == "S" or resp == "s":
           # grambamos el cambio en la tarea 
           DicTarjetas.pop(tarea_Seleccion)
           print("tarea borrada")        
           temresp = input ("Pulse enter para continuar")
        else:
           # anulamos el cambio en la tarea
           print("Borrado cancelado")        
           temresp = input ("Pulse enter para continuar")            
    else:
        # La Tarea seleccionada no existe 
        print("La tarea que esta intenando seleccionar no existe")        
        temresp = input ("Pulse enter para continuar")

# =========
# START 
# =========
continuar = True
while continuar:
    os.system("Cls")
    print("==================================")
    print("     1.- Listar Tareas")
    print("     2.- Cambiar Estado Tarea")
    print("     3.- Crear Tarea")
    print("     4.- Borrar Tarea")
    print("     5.- Salir")
    print("==================================")
    print("")

    Resp = input ("Elija una opcion de la lista _:")
    if Resp == "1": 
       Pantall_Listar_Tareas(DicTarjetas)

    elif Resp == "2":
       Pantalla_Cambio_Estado(DicTarjetas)
        
    elif Resp == "3":
       Indice =  pantalla_crearTarea(Indice)

    elif Resp == "4":
        Pantalla_Borrado_Tarea(DicTarjetas)

    elif Resp == "5":
        continuar = False
        print()
        print("==================================")
        print ("Fin de programa")
        print("==================================")

    else:
        print ("")
        print ("Error, opcion no valida, elija otra opcion")
        temresp = input ("Pulse enter para continuar")


# =========
# End
# =========

