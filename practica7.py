from typing import List

# 1.1
def pertenece1(s: List[int], e: int) -> bool:
    return e in s

# print(pertenece1([1,2,3], 4))

def pertenece2(s: List[int], e: int) -> bool:
    for i in range(0, len(s), 1):
        if (e == s[i]):
            return True
    return False

# print(pertenece2([1,2,3], 2))

def pertenece3(s: List[int], e: int) -> bool:
    for i in s:
        if (e == i):
            return True
    return False

# print(pertenece3([1,2,3],5))

# 1.2
def divide_a_todos(s: List[int], e: int) -> bool:
    if e == 0:
        return
    for i in s:
        return i % e == 0
    
# print(divide_a_todos([12,6,9], 3))

# 1.3
def suma_total(s: List[int]) -> int:
    count: int = 0
    for i in s:
        count += i
    return count
    
# print(suma_total([2,123,1]))

# 1.4
def ordenados(s: List[int]) -> bool:
    i: int = 0

    while (i + 1 < len(s)):
        for n in s:
            if (s[i] > s[i + 1]):
                return False
        i += 1
        
    return True
    
# print(ordenados([3,1,8]))

# 1.5
def longitud_mayor_a_7(s: List[str]) -> bool:
    for p in s:
        if len(p) > 7:
            return True
    return False

# print(longitud_mayor_a_7(["aaaaaaad"]))

# 1.6
def palindromo(palabra: str) -> bool:
    
    for i in range(0,len(palabra),1):
        if palabra[i] != palabra[len(palabra)-1-i]:
            return False
    
    return True

# print(palindromo("hoiiioh"))

# 1.7
def tiene_minuscula(palabra: str) -> bool:
    for i in palabra:
        if i >= 'a' and i <= 'z':
            return True
    return False

def tiene_mayuscula(palabra: str) -> bool:
    for i in palabra:
        if i >= 'A' and i <= 'Z':
            return True
    return False

def tiene_numero(palabra: str) -> bool:
    for i in palabra:
        if i >= '0' and i <= '9':
            return True
    return False

def fortaleza(palabra: str) -> str:
    if len(palabra) < 5:
        return "ROJA"
    elif len(palabra) > 8 and tiene_minuscula(palabra) and tiene_mayuscula(palabra) and tiene_numero(palabra):
        return "VERDE"
    else:
        return "AMARILLA"
    
# print(fortaleza("holaa997874PPPP8234"))

# 1.8
def saldo(mov: List[tuple]) -> float:
    count: float = 0
    for tupla in mov:
        if tupla[0] == "I":
            count += tupla[1]
        elif tupla[0] == "R":
            count -= tupla[1]
    return count

# print(saldo([("I",200),("I",300),("R",150),("I",1000),("R",50)]))

# 2.1
def posiciones_pares_0(lista: List[float]) -> List[float]:
    for i in range(0,len(lista)):
        if i % 2 == 0:
            lista[i] = 0
    return lista

# print(posiciones_pares_0([1,4,3,9,5,7]))

# 2.2
def posiciones_pares_0_2(lista: List[float]) -> List[float]:
    lista2: List[float] = []
    for i in range(0, len(lista)):
        if i % 2 == 0:
            lista2.append(0)
        else:
            lista2.append(lista[i])
    return lista2

# print(posiciones_pares_0_2([1,4,3,9,5,7]))

# 2.3
def es_vocal(letra: str) -> bool:
    return letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U"

def cadena_sin_vocales(cadena: str) -> str:
    cadena_nueva: str = ""
    for i in range(0, len(cadena)):
        if not es_vocal(cadena[i]):
            cadena_nueva += cadena[i]
    return cadena_nueva

# print(cadena_sin_vocales("hola madre"))

# 2.4
def reemplaza_vocales(cadena: str) -> str:
    cadena_nueva: str = ""
    for i in range(0, len(cadena)):
        if not es_vocal(cadena[i]):
            cadena_nueva += cadena[i]
        else:
            cadena_nueva += "_"
    return cadena_nueva

# print(reemplaza_vocales("hipOOOOOlaaaa"))

# 2.5
def da_vuelta_str(s: str) -> str:
    invertido: str = ""
    for i in range(0, len(s)):
        invertido += s[len(s) - i - 1]
    return invertido

# print(da_vuelta_str("hola"))

# 2.6
def eliminar_repetidos(s: str) -> str:
    salida: str = ""
    for i in range(0, len(s)):
        if s[i] not in salida:
            salida += s[i]
    return salida

# def eliminar_repetidos(s: str) -> str:
#     salida: str = ""
#     for i in s:
#         if i not in salida:
#             salida += i
#     return salida

# print(eliminar_repetidos("kkkkkkkkhaaaaaaaolaa"))

# 3
def promedio(notas: List[int]) -> float:
    return suma_total(notas) / len(notas)

def alguno_menor_a_4(notas: List[int]) -> bool:
    for nota in notas:
        if nota < 4:
            return True
    return False

def aprobado(notas: List[int]) -> int:
    if not alguno_menor_a_4(notas) and promedio(notas) >= 7:
        return 1
    elif not alguno_menor_a_4(notas) and promedio(notas) >= 4 and promedio(notas) < 7:
        return 2
    elif alguno_menor_a_4(notas) or promedio(notas) < 4:
        return 3
    
        
# print(aprobado([8,4,2]))

# 4.1
def estudiantes() -> List[str]:
    res: List[str] = []
    nombre = input("ingrese el nombre de un estudiante \n")
    while nombre != "listo":
        res.append(nombre)
        nombre = input()
    return res

# print(estudiantes())

# 4.2
def monedero() -> List[tuple]:
    historial: List[tuple] = []
    operacion = input("ingrese la operacion que desee realizar \n")

    while operacion != "X":
        if operacion == "C":
            monto_cargar = input("ingrese el monto que desee cargar \n")
            historial.append((operacion, monto_cargar))
            operacion = input("ingrese la operacion que desee realizar \n")
        elif operacion == "D":
            monto_descontar = input("ingrese el monto que desee descontar \n")
            historial.append((operacion, monto_descontar))
            operacion = input("ingrese la operacion que desee realizar \n")
    return historial

# print(monedero())

# 4.3

# 5.1
def pertenece_a_cada_uno_v1(s: List[List[int]], e: int) -> List[bool]:
    res: List[bool] = []
    for i in range(0, len(s)):
        res.append(pertenece1(s[i], e))
    return res

# print(pertenece_a_cada_uno_v1([[1,2,3], [1,2,3], [1,3,4], [1,2,3,2], [4,4,4]], 2))

