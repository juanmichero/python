from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import List
import random

# Ejercicio 2
def clonar_cola(cola: Cola) -> Cola:
    copy_cola: Cola = Cola()
    elementos: list = []

    while not cola.empty():
        elem = cola.get()
        elementos.append(elem)
        copy_cola.put(elem)

    for elem in elementos:
       cola.put(elem)

    return copy_cola

def orden_de_atencion (urgentes: Cola[int], postrgables: Cola[int]) -> Cola[int]:
    urgentes_copy: Cola = clonar_cola(urgentes)
    postrgables_copy: Cola = clonar_cola(postrgables)
    urgentes_list: list = []
    postrgables_list: list = []
    res: Cola = Cola()

    while not urgentes_copy.empty():
        paciente = urgentes_copy.get()
        urgentes_list.append(paciente)

    while not postrgables_copy.empty():
        paciente = postrgables_copy.get()
        postrgables_list.append(paciente)

    for i in range(len(urgentes_list)):
       res.put(urgentes_list[i])
       res.put(postrgables_list[i])

    return res

#cola1=Cola()
#cola2=Cola()
#cola1.put(2)
#cola1.put(4)
#cola1.put(6)
#cola2.put(1)
#cola2.put(3)
#cola2.put(5)
#print(orden_de_atencion(cola2, cola1).queue)

# Ejercicio 3
def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
    res: list = []
    ocupaciones: list = []

    for i in range(len(camas_por_piso)):
        camas = camas_por_piso[i]
        camas_ocupadas_por_piso: int = 0
        for j in range(len(camas)):
            if camas[j] == True:
                camas_ocupadas_por_piso += 1
        ocupaciones.append(camas_ocupadas_por_piso)

    for k in range(len(ocupaciones)):
        res.append(ocupaciones[k] / len(camas_por_piso[k]))

    return res


def cant_elementos(c: Cola) -> int:
    c_copy = clonar_cola(c)
    count: int = 0

    while not c_copy.empty():
        c_copy.get()
        count += 1
    return count

colaagus=Cola()
colaagus.put(1)
colaagus.put(1)
colaagus.put(1)
colaagus.put(1)
colaagus.put(1)
colaagus.put(1)
colaagus.put(1)
colaagus.put(1)
colaagus.put(1)
colaagus.put(1)
#print(colaagus.queue)
#print(cant_elementos(colaagus))


def clonar_pila(p: Pila) -> Pila:
    nueva_pila: Pila = Pila()
    elementos = []
    while not p.empty():
        elementos.append(p.get())
    
    for elemento in reversed(elementos):
        nueva_pila.put(elemento)
        p.put(elemento)
    
    return nueva_pila

# imprimir_pila(clonar_pila(p))

def cant_elem(p: Pila) -> int:
    count: int = 0
    copy: Pila = clonar_pila(p)

    while not copy.empty():
        copy.get()
        count += 1
    return count

pila: Pila = Pila() 
pila.put(1)
pila.put(2)
pila.put(3)

print("creo la pila")
print(pila.queue)
print("le pedi la cantidad")
print(cant_elem(pila))
print("tuki")
print(cant_elem(pila))

def nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c = Cola()
    for i in range(cantidad):
        nro: int = random.randint(desde, hasta)
        c.put(nro)
    return c

print(nros_al_azar(10, 0, 1).queue)

