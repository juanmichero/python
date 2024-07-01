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

# Ejercicio 4
# dict = { 123: [2, 5, 10], 234: [3, 1, 7], 345: [1, 2, 5] }
# res = [123] (17 horas)

def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    max_horas: int = 0
    res: list[int] = []

    for clave, valor in horas.items():
        suma_horas: int = 0

        for hora in valor:
            suma_horas += hora

        if suma_horas > max_horas:
            max_horas = suma_horas
            res = [clave]
        elif suma_horas == max_horas:
            res.append(clave)
        
    return res

# print(empleados_del_mes({123: [2, 5, 10], 234: [3, 1, 7], 345: [1, 2, 5], 111: [10, 7]}))

########################################

# 1)
# dict = { "juan": [15, 30, 45] } ---> { "juan": (3, 30) }

def promedio_salas(tiempos: list[int]) -> tuple[int, float]:
    res: tuple[int, float] = 0
    cantidad_tiempos: int = 0
    promedio_tiempos: float = 0

    for tiempo in tiempos:
    
        if tiempo > 0 and tiempo < 61:
            cantidad_tiempos += 1
            promedio_tiempos += tiempo
        
    promedio_tiempos /= cantidad_tiempos

    res = (cantidad_tiempos, promedio_tiempos)
    
    return res

def promedio_de_salidas(registro: dict[str, list[int]]) -> dict[str, tuple[int, float]]:
    res: dict[str, tuple[int, float]] = {}

    for nombre, tiempos in registro.items():
        promedio_tiempos: float = promedio_salas(tiempos)[1]
        cantidad_salas: int = promedio_salas(tiempos)[0]

        res[nombre] = (cantidad_salas, promedio_tiempos)

    return res
    
# print(promedio_de_salidas({ "juan": [15, 30, 45], "pedro": [1, 20, 40], "carlos": [60, 30, 61] }))

# 2)
# list = [ 20, 15, 60, 61, 48 ] ---> 1

def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    tiempos_filtrados: list[int] = []
    res: int = 0

    for tiempo in tiempos_salas:
        if tiempo > 0 and tiempo < 61:
            tiempos_filtrados.append(tiempo)

    minimo = tiempos_filtrados[0]
    
    for indice in range(len(tiempos_filtrados)):
        tiempo = tiempos_filtrados[indice]

        if tiempo < minimo:
            minimo = tiempo
            res = indice
    
    return res

# print(tiempo_mas_rapido([0, 20, 15, 20, 61]))

# 3)
# list = [ 20, 15, 60, 61, 48 ] ---> 

# 4)
# list = [ 
#   [ 12, 8, 47, 20 ],
#   [ 0, 0, 12, 0 ],
#   [ 2, 0, 0, 51 ] 
# ] 
# ---> [ 1 ]

def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    res: list[int] = []

    for i in range(len(amigos_por_salas)):
        sala = amigos_por_salas[i]
        if sala[0] == 0 and sala[1] == 0 and sala[3] == 0 and sala[2] > 0:
            res.append(i)

    return res

# print(escape_en_solitario([
#     [1, 2, 3, 4],
#     [0, 0, 28, 0],
#     [0, 61, 61, 0],
# ]))

#####################################

# 1)
# list = [ ( "caca", 20 ), ( "pis", 7 ), ( "caca", 15 ), ( "pis", 1 ) ] 
# ---> { "caca": (15, 20), ( "pis": (1, 7) ) }

def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    res: dict[str, tuple[int, int]] = {}

    for producto in stock_cambios:
        nombre = producto[0]
        stock = producto[1]

        if nombre in res.keys():
            producto_res = res[nombre]

            if stock < producto_res[0]:
                res[nombre] = (stock, producto_res[1])
            elif stock > producto_res[1]:
                res[nombre] = (producto_res[0], stock)
        
        else:
            res[nombre] = (stock, stock)

    return res

# print(stock_productos([ ( "caca", 20 ), ( "pis", 7 ), ( "pis", 29 ), ( "caca", 15 ), ( "pis", 1 ), ( "caca", 2 ), ( "moco", 123 ) ]))

# 2)
def es_primo(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def ultimos_3(num: int) -> int:
    return num % 1000
    
def filtrar_codigos_primos(codigos_barra: List[int]) -> List[int]:
    primos: List[int] = []
    for numero in codigos_barra:
        if es_primo(ultimos_3(numero)):
            primos.append(numero)
    return primos

# print(filtrar_codigos_primos([7, 40, 203003]))

# 3)
def subsecuencia_mas_larga(tipos_pacientes_atendidos: List[str]) -> int:
    max_repeticiones: int = 1
    repeticiones_actuales: int = 1
    elemento_actual: str = tipos_pacientes_atendidos[0]

    for i in range(1, len(tipos_pacientes_atendidos)):
        if tipos_pacientes_atendidos[i] == elemento_actual:
            repeticiones_actuales += 1
        else:
            if repeticiones_actuales > max_repeticiones:
                max_repeticiones = repeticiones_actuales
            elemento_actual = tipos_pacientes_atendidos[i]
            repeticiones_actuales = 1
            
    if repeticiones_actuales > max_repeticiones:
        max_repeticiones = repeticiones_actuales
        
    return max_repeticiones

# print(subsecuencia_mas_larga(["perro", "perro", "gato", "gato", "gato", "gato"]))

def subsecuencia_mas_larga_2(tipos_pacientes_atendidos: List[str]) -> int:
    cant: int = 0
    max_cant: int = 0
    res: int
    for i in range(len(tipos_pacientes_atendidos)):
        if tipos_pacientes_atendidos[i] == "perro" or tipos_pacientes_atendidos[i] == "gato":
            cant += 1
        else:
            if cant > max_cant:
                max_cant = cant
                res = i - cant
                cant = 0
    if cant > max_cant:
        max_cant = cant
        res = i - (cant - 1)

    return res


# 4)

# turnos = [
#             ["Ana", "Ana", "Sol", "Ana", "Sol", "Sol"],    # 9-10
#             ["Ana", "aNa", "Sol", "Ana", "Ana", "Ana"],    # 10-11
#             ["Ana", "Ana", "Sol", "Sol", "Ana", "Ana"],    # 11-12
#             ["Ana", "Ana", "Sol", "Sol", "Ana", "Ana"],    # 12-13
#             ["Luis", "Luis", "Luis", "Luis", "Luis", "Sol"],    # 14-15
#             ["Luis", "Sol", "Luis", "Luis", "Luis", "Sol"],    # 15-16
#             ["Luis", "Luis", "Luis", "Luis", "Sol", "Sol"],    # 16-17
#             ["Luis", "Sol", "Luis", "Ana", "Luis", "Sol"]     # 17-18
#         ]
def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool, bool]]:
    res: list[tuple[bool, bool]] = []

    