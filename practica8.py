from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
from typing import List

# 1.1
def contar_lineas(archivo: str) -> int:
    file = open(archivo, "r", encoding='utf-8')
    res: int = len(file.readlines())
    file.close()
    return res

# print(contar_lineas("hola.txt"))

# 1.2
def existe_palabra(palabra: str, archivo: str) -> bool:
    file = open(archivo, "r", encoding='utf-8')
    contenido = file.readlines()
    for line in contenido:
        if palabra in line:
            file.close()
            return True
    file.close()
    return False
    # if palabra in contenido:
    #     return True
    # else:
    #     return False
    
# print(existe_palabra("hola", "hola.txt"))

# 1.3
def cantidad_apariciones(palabra: str, archivo: str) -> int:
    file = open(archivo, "r", encoding='utf-8')
    contenido = file.readlines()
    res: int = 0
    for line in contenido:
        if palabra in line:
            res += 1
    file.close()
    return res

# print(cantidad_apariciones("hola", "hola.txt"))
# !!!!!!!!!!!!!!!!!!!!!!!!!!

# 2
def clonar_sin_comentarios(archivo: str):
    file = open(archivo, "r", encoding='utf-8')
    contenido = file.read()
    new_file = open("clonado.txt", "a", encoding='utf-8')
    new_file.write(contenido)
    file.close()
    new_file.close()

# clonar_sin_comentarios("hola.txt")

###################

# 8
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p = Pila()
    for i in range(cantidad):
        nro: int = random.randint(desde, hasta)
        p.put(nro)
    return p

def imprimir_pila(pila):
    while not pila.empty():
        elem: int = pila.get()
        print(elem)

def print_pila(pila):
    copy: Pila = clonar_pila(pila)
    while not copy.empty():
        elem = copy.get()
        print(elem)

# imprimir_pila(generar_nros_al_azar(5, 1, 100))

# 9
def cantidad_elementos(p: Pila) -> int:
    count: int = 0
    while not p.empty():
        p.get()
        count += 1
    return count

# pila: Pila = generar_nros_al_azar(125, 1, 10)
# print(cantidad_elementos(pila))

def clonar_pila(p: Pila) -> Pila:
    nueva_pila: Pila = Pila()
    elementos = []
    while not p.empty():
        elementos.append(p.get())
    
    for elemento in reversed(elementos):
        nueva_pila.put(elemento)
        p.put(elemento)
    
    return nueva_pila

# p: Pila = Pila()
# p.put(1)
# p.put(2)
# p.put(3)
# imprimir_pila(clonar_pila(p))

def cant_elem(p: Pila) -> int:
    count: int = 0
    copy: Pila = clonar_pila(p)

    while not copy.empty():
        copy.get()
        count += 1
    return count

# print("creo la pila")
# pila: Pila = generar_nros_al_azar(15, 1, 100)
# print(cant_elem(pila))
# print("le pedi la cantidad")
# print_pila(pila)
# print("tuki")
# print(cant_elem(pila))

# 10
def buscar_el_maximo(pila: Pila[int]) -> int:
    max_valor = pila.get()
    pila_aux = Pila()
    pila_aux.put(max_valor)
    
    while not pila.empty():
        item = pila.get()
        if item > max_valor:
            max_valor = item
        pila_aux.put(item)
    
    while not pila_aux.empty():
        pila.put(pila_aux.get())
    
    return max_valor

# pila = Pila()
# pila.put(17)
# pila.put(7)
# pila.put(19)
# pila.put(1)

# print(buscar_el_maximo(pila))

# 11
# def esta_bien_balanceada(s: str) -> bool:
#     pila = Pila()
#     i: int = 0
#     val: bool = True
#     while i < len(s):
#         if s[i] == '(':
#             pila.put(1)
#         elif s[i] == ')' and not pila.empty():
#             pila.get()
#         else:
#             val = False
#         i += 1
#     return val and pila.empty()

# print(esta_bien_balanceada(""))

def esta_bien_balanceada(s: str) -> bool:
    pila = Pila()
    for char in s:
        if char == '(':
            pila.put(char)
        elif char == ')':
            if pila.empty() or pila.get() != '(':
                return False
    return pila.empty()

# print(esta_bien_balanceada("1 + 2 + (8*2)"))

# 12
def evaluar_expresion(expresion: str) -> float:
    operadores: List[str] = ['+', '-', '*', '/']
    operandos: Pila[str] = Pila()
    for char in expresion:
        if char in operadores:
            if char == "+":
                operandos.put(float(operandos.get()) + float(operandos.get()))
            if char == "-":
                operandos.put(float(operandos.get()) - float(operandos.get()))
            if char == "*":
                operandos.put(float(operandos.get()) * float(operandos.get()))
            if char == "/":
                operandos.put(float(operandos.get()) / float(operandos.get()))
        elif char != " ":
            operandos.put(char)
    return operandos.get()


# print(evaluar_expresion("3 4 + 5 * 2 -"))

# 13
def nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c = Cola()
    for i in range(cantidad):
        nro: int = random.randint(desde, hasta)
        c.put(nro)
    return c

def clonar_cola(c: Cola) -> Cola:
    nueva_cola: Cola = Cola()
    elementos = []
    while not c.empty():
        elementos.append(c.get())
    
    for elemento in elementos:
        nueva_cola.put(elemento)
        c.put(elemento)
    
    return nueva_cola

def print_cola(cola):
    copy: Cola = clonar_cola(cola)
    while not copy.empty():
        elem = copy.get()
        print(elem)

# print_cola(nros_al_azar(10, 1, 20))

# 14
def cant_elementos(c: Cola) -> int:
    c_copy = clonar_cola(c)
    count: int = 0

    while not c_copy.empty():
        c_copy.get()
        count += 1
    return count

# cola: Cola = nros_al_azar(10, 10, 10)
# print(cant_elementos(cola))
# print(cant_elementos(cola))

# def print_cola2(cola):
#     while not cola.empty():
#         elem = cola.get()
#         print(elem)

# print("creo la cola")
# cola: Cola = nros_al_azar(5, 1, 100)
# print(cant_elementos(cola))
# print("le pedi la cantidad")
# print_cola2(cola)
# print("tuki")
# print(cant_elementos(cola))

# 15
def maximo(c: Cola[int]) -> int:
    cola: Cola = Cola()
    maximo = None
    while not c.empty():
        elemento = c.get()
        if maximo == None or elemento > maximo:
            maximo = elemento
        cola.put(elemento)
    while not cola.empty():
        c.put(cola.get())
    return maximo

# c: Cola = nros_al_azar(10, 1, 100)
# print_cola(c)
# print("MAXIMOOOO")
# print(maximo(c))

# 16 
def armar_secuencia_bingo() -> Cola[int]:
    cola: Cola = Cola()
    nums: list = list(range(100))
    random.shuffle(nums)
    for num in nums:
        cola.put(num)
    return cola

def jugar_carton_bingo(carton: List[int], bolillero: Cola[int]) -> int:
    count: int = 0

    while len(carton) > 0:
        num = bolillero.get()
        if num in carton:
            carton.remove(num)
        count += 1
    return count

# print("bolillero:")
# cola: Cola = armar_secuencia_bingo()
# print_cola(cola)
# print("jugadas:")
# print(jugar_carton_bingo([1,2,3,4,5], cola))

# 17
def n_pacientes_urgentes(c: Cola[(int, str, str)]) -> int:
    count: int = 0
    while not c.empty():
        pedido = c.get()
        if pedido[0] >= 1 and pedido[0] <= 3:
            count += 1
    return count

# cola: Cola = Cola()
# cola.put((5, "pepe", "pis"))
# cola.put((1, "carlos", "caca"))
# cola.put((5, "pepe", "pis"))
# cola.put((3, "sebastian", "pie"))
# cola.put((8, "juan", "tenedor"))
# print(n_pacientes_urgentes(cola))

# 18
#############

#######################################################################

# 1)
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

# 4)

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

#########################

# 1)
def reordenar_cola_priorizando_vips(filaClientes: Cola[(str, str)]) -> Cola[str]:
    cola_comun: Cola = Cola()
    cola_vip: Cola = Cola()
    cola_final: Cola = Cola()

    while not filaClientes.empty():
        elem = filaClientes.get()
        if elem[1] == "comun":
            cola_comun.put(elem[0])
        elif elem[1] == "vip":
            cola_vip.put(elem[0])

    while not cola_vip.empty():
        vip = cola_vip.get()
        cola_final.put(vip)
    while not cola_comun.empty():
        comun = cola_comun.get()
        cola_final.put(comun)


    # for cliente in filaClientes:
    #     if cliente[1] == "comun":
    #         cola_comun.put(cliente[0])
    #     elif cliente[1] == "vip":
    #         cola_vip.put(cliente[0])

    
    return cola_final

# cola: Cola = Cola()
# cola.put(("juan","vip"))
# cola.put(("carlos","comun"))
# cola.put(("josefino","comun"))
# cola.put(("pedro","vip"))
# cola.put(("pepe","vip"))
# cola.put(("huh","comun"))
# print_cola(cola)

# print_cola(reordenar_cola_priorizando_vips(cola))

# print_cola(cola)

# 4)


# def cuantos_sufijos_son_palindromos(texto: str) -> int:
