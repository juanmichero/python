#Ejercicio 1

def ind_nesima_aparicion (s: list[int], n: int, elem: int) -> int:
    numero_apariciones: int = 0
    posicion: int = -1
    numero_apariciones_igual_n: bool = False
    i: int = 0
    while i < len(s) and numero_apariciones_igual_n == False:
        if (s[i] == elem):
            numero_apariciones += 1
        if (numero_apariciones == n):
            posicion = i
            numero_apariciones_igual_n = True
        i += 1
        
    return posicion

#Ejercicio 2

def mezclar(s1: list[int], s2: list[int]) -> list[int]:
    res: list[int] = []
    for i in range(len(s1)):
        res.appennd(s1[i])
        res.appennd(s2[i])

    return res

#Ejercicio 3

def crear_lista_n_elementos(n: int) -> list[int]:
    res: list[int] = []
    while n > 0:
        res.append(0)
        n -= 1
    return res


def frecuencia_posiciones_por_caballo(lista_caballos: list[str], dict_carreras: dict[(str, list[str])]) -> dict[(str, list[int])]:
    res: dict[(str, list[int])] = {}
    
    for caballo in lista_caballos: #caballo es de tipo str
        carrera_caballo: list[int] = crear_lista_n_elementos(len(lista_caballos))
        for carrera_nombre in dict_carreras.keys(): # carrera es de tipo str 
            se_encontro_caballo: bool = False
            i: int= 0
            carrera: list[str] = dict_carreras[carrera_nombre]
            while (i < len(carrera)) and (se_encontro_caballo == False):
                if (carrera[i] == caballo):
                    se_encontro_caballo = True
                    carrera_caballo[i] += 1 # Se que las carreras tienen la misma cantidad de elementos que las listas que cree para los caballos
                i += 1
        res[caballo] = carrera_caballo
    return res

#Ejercicio 4

def es_capicua(lista: list[int]) -> bool:
    return lista == lista_invertida(lista)

def lista_invertida(lista: list[int]) -> list[int]:
    res: list[int] = []
    for i in lista:
        res = [i] + res
    return res

def matriz_capicua(matriz: list[list[int]]) -> bool:
    es_matriz_capicua: bool = True
    for lista in matriz:
        if (not es_capicua(lista)):
            es_matriz_capicua = False
    return es_matriz_capicua
