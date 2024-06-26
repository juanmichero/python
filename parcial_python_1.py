from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import List

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