from queue import Queue as Cola
import random

def generar_numeros_al_azar(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    res:Cola[int] = Cola()
    for i in range(cantidad):
        n:int = random.randint(desde, hasta)
        # print(n)
        res.put(n)
    return res

# imprimir_cola (in c: Cola[int])
def imprimir_cola(c: Cola[int]) -> None:
    lista:list[int] = []
    while not c.empty():
        lista.append(c.get())
        
    for i in lista:
        c.put(i)
    print(lista)

# res:Cola[int] = generar_numeros_al_azar(3, 0, 10)
# imprimir_cola(res)
# imprimir_cola(res)

def dame_lista_palabras(linea:str)->list[str]:
    # require: linea no tiene espacios al ppio ni al final
    res:list[str] = []
    palabra_en_construccion:str = ""
    for letra in linea:
        if letra != " ":
            palabra_en_construccion = palabra_en_construccion+letra
        else:
            if len(palabra_en_construccion) > 0:
                res.append(palabra_en_construccion)
                palabra_en_construccion = ""
    res.append(palabra_en_construccion)
    return res

print(dame_lista_palabras("Hola mundo compu"))

def agrupar_por_longitud(texto: str) -> dict[int, int]:
    res:dict[int,int] = dict()
    palabras:list[str] = dame_lista_palabras(texto)
    for palabra in palabras:
        longitud:int = len(palabra)
        if longitud in res.keys():
            res[longitud] = res[longitud] + 1
        else:
            res[longitud] = 1
    return res

def agrupar_por_longitud2(texto: str) -> dict[int, list[str]]:
    res:dict[int,list[str]] = dict()
    palabras:list[str] = dame_lista_palabras(texto)
    for palabra in palabras:
        longitud:int = len(palabra)
        if longitud in res.keys():
            res[longitud].append(palabra)
        else:
            res[longitud] = [palabra]
    return res

agrupar_por_longitud2("Hola mundo compu")