from Grafo.Grafo import *
import json

grafo = Grafo(True)
# grafo.ingresarN("Tierra")
# grafo.ingresarN("Venus")
# grafo.ingresarN("Jupiter")
# grafo.ingresarN("Mercurio")
# grafo.ingresarN("Marte")
# grafo.ingresarN("Saturno")
# grafo.ingresarN("Urano")
# grafo.ingresarN("Neptuno")
# grafo.ingresarN("Pluton")
# grafo.ingresarA("Tierra", "Venus",10)
# grafo.ingresarA("Tierra", "Saturno",20)
# grafo.ingresarA("Saturno", "Marte", 10)
# grafo.ingresarA("Saturno", "Venus", 20)
# grafo.ingresarA("Venus", "Jupiter", 1)
# grafo.ingresarA("Saturno", "Urano", 1)
# grafo.ingresarA("Jupiter", "Mercurio", 1)
# grafo.ingresarA("Mercurio", "Pluton", 1)
# grafo.ingresarA("Mercurio", "Neptuno", 1)

# grafo.imprimirN()
# grafo.imprimirA()
# pozos = grafo.buscarPozos()
# fuentes = grafo.buscarFuentes()
# gradoF = grafo.gradoNodo("F")
# print(pozos)
# print(fuentes)
# print(f"El grado del nodo F es {gradoF}")
# grafo.imrpimirAdyacencia("F")
grafo.cargarGrafoJSON("./Data/planets.json")
print(grafo.esConexo())
print(".....................")
grafo.caminoMasCorto("Tierra","Neptuno")
print("8. Conocer si la Galaxia está fuertemente Conectada")
print("9. Conocer si hay planetas sin rutas salientes (pozos)")
print("10. Conocer las rutas que entran y salen de cada planeta")
print("11.  Obstruir Ruta")
print("12. Conocer si hay planetas sin rutas salientes (pozos)")
print("13. Conocer las rutas que entran y salen de cada planeta")
option=-1

elif option=="5":
    print("dijite el nombre del planeta a elimiar del sistema: ")
    eliminar=input()
    grafo.eliminarNodo(eliminar)
elif option=="6":
    print("Para eliminar la ruta, digite el planeta origen y el planeta destino")
    print("Origen")
    origen=input()
    print("Destino")
    destino=input()
    grafo.eliminarArista(origen,destino)

    #Este es para obstruir o habilitar una ruta en la galxia
if option=="":
    print("Para obstruir o habilitar una ruta, debe ingresar el origen y  el destino ")
    print("si desea obtruir una ruta, presione 1, o 2 para habilitarla")
    control=input()
    decision= True if control=1 else False
   grafo.controlarObstruccionArista(origen,destino,decision)

#Invierte el origen y destino de una ruta (Arista)
if option=="":
    print("Para Modifica el sentido de una ruta, debe digitar el planeta origen y el planeta destino")
    print("Origen")
    origen=input()
    print("Destino")
    destino=input()
    grafo.invertirArista(origen,destino)
    #Recorrido en amplitud y profundidad
if option=="":
    print("Para conocer las rutas de las naves debe seleccionar si será recorrido en Anchura o Profundidad, presione 1 para Anchura o 2 para Profundidad")
    recorrido=input()
    if recorrido==1:
       print(grafo.amplitud)
    if recorrido==2:
        print (grafo.profundidad)
    else:
        print("Opción Incorrecta")
        #Árbol de expansión mínima kruskal y boruvka
if option=="":
    print("Acá puede ver los recorridos mínimos que puede hacer una nave para recorrer todos los planetas")
    print("Recorrido iniciando por la conexión menor")
    grafo.kruskal
    print()
    print("Recorrido iniciando por la lista de planetas en orden de creaeción el el sistema")
    grafo.boruvka
     #Menor recorrido de una planeta a otro, dijsktra
    if option=="":
        print("Acá podrá ver el recorrido que le tomara menos tiempo desde un planeta origen que elija a uno destino ")
        print("Origen")
        origen=input()
        print("Destino")
        destino=input()
        grafo.caminoMasCorto(origen,destino)
    