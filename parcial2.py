def cuantos_sufijos_son_palindromos(texto:str) -> int:
    res: int = 0
    listaChar: list[chr] = []
    # Creo una lista con los chars
    for letra in texto:
        listaChar.append(letra)
    
    #Chequear todos los casos
    for i in range(0, len(texto)):
        palabraIterada: str = ""
        for letra in listaChar:
            palabraIterada += letra
        if (es_palindromo(palabraIterada)):
            res += 1
        listaChar.pop(0)
    return res

def es_palindromo(palabra: str) -> bool:
    inversoPalabra: str = palabra[::-1] # si no se puede usar esto, uso invertir_palabra()
    print(inversoPalabra)
    if(palabra == inversoPalabra):
        return True
    return False


def invertir_palabra(palabra: str) -> str:
    res = ""
    for i in range(len(palabra) - 1, -1, -1):
        res += palabra[i]
    return


#1 de otro parcial

def es_primo(num: int) -> bool:
    if(num <= 1): return False
    for i in range (2, int(num/2)):
        if(num % i == 0): return False
    return True

def filtrar_codigos_primos(codigos: list[int]) -> list[int]:
    res: list[int] = []
    for codigo in codigos:
        _3digitos:int = codigo % 1000
        if(es_primo(_3digitos)):
            res.append(codigo)
    return res

#2

def stock_productos(stock_cambios: list[(str, int)]) -> dict[str, (int, int)]:
    res: dict[str, (int, int)] = {}
    for tupla in stock_cambios:
        producto = tupla[0]
        cantidad = tupla[1]
        keys: list[str] = []
        for key in res.keys():
            keys.append(key)
        if(producto in keys):
            maximo = res[producto][1]
            minimo = res[producto][0]
            if(cantidad > maximo):
                res[producto] = (minimo, cantidad)
            elif(cantidad < minimo):
                res[producto] = (cantidad, maximo)
        else: 
            res[producto] = (cantidad, cantidad)
    return res

#print(stock_productos([("Galletas", 5), ("Perros", 5), ("Gatos", 5), ("Ludopatas", 5), ("Galletas", 10), ("Galletas", 100)]))

#3

# [    LUN MAR  MIE  JU  VI  SA  DO 
# 9hs  [L, MAR, MIE, JU, VI, SA, DO]
# 10hs [L, MAR, MIE, JU, VI, SA, DO]
# 11hs [L, MAR, MIE, JU, VI, SA, DO]
# 12hs [L, MAR, MIE, JU, VI, SA, DO]
# 14hs [L, MAR, MIE, JU, VI, SA, DO]
# 15hs [L, MAR, MIE, JU, VI, SA, DO]
# 16hs [L, MAR, MIE, JU, VI, SA, DO]
# 17hs [L, MAR, MIE, JU, VI, SA, DO]
# ]

def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[(bool, bool)]:
    res: list[(bool, bool)] = []
    for dia in range(0, len(grilla_horaria[0])):
        manianaSeguida: bool = True
        ultimoNombreChequeado: str = grilla_horaria[0][dia]
        for horario in range(0, 4):
            if(grilla_horaria[horario][dia] != ultimoNombreChequeado): manianaSeguida = False
        tardeSeguida: bool = True
        ultimoNombreChequeado = grilla_horaria[4][dia]
        for horario in range(4, 7):
            if(grilla_horaria[horario][dia] != ultimoNombreChequeado): tardeSeguida = False
        res.append((manianaSeguida, tardeSeguida))
    return res
#*print(un_responsable_por_turno([

    ["A", "A", "A", "A", "B", "A", "B"],
    ["A", "A", "A", "A", "B", "A", "A"],
    ["A", "A", "A", "B", "B", "A", "A"],
    ["A", "B", "A", "B", "A", "A", "A"],
    
    ["A", "A", "B", "B", "B", "A", "B"],
    ["A", "A", "A", "B", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A", "A"]
#]))

# Ejercicio 4

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    lastIndexWasDogOrCat: bool = False
    lastLongestIndex: int = 0
    currentCountingIndex: int = 0
    lastLongestIndexLength: int = 0
    currentCountingIndexLength: int = 0
    for i in range(0, len(tipos_pacientes_atendidos)):
        currentAnimal: str = tipos_pacientes_atendidos[i]
        #Chequeamos si empieza una secuencia nueva
        if(not lastIndexWasDogOrCat):
            if(currentAnimal == "perro" or currentAnimal == "gato"):
                lastIndexWasDogOrCat = True
                currentCountingIndexLength += 1
                currentCountingIndex = i
        #Esta contunuando una secuencia
        else:
            #La secuencia sigue
            if(currentAnimal == "perro" or currentAnimal == "gato"):
                currentCountingIndexLength += 1
            #la secuencia se corto
            else:
                currentCountingIndexLength = 0
                lastIndexWasDogOrCat = False
        
        #Updatear valores
        if(currentCountingIndexLength > lastLongestIndexLength):
            lastLongestIndexLength = currentCountingIndexLength
            lastLongestIndex = currentCountingIndex
    
    return lastLongestIndex

print(subsecuencia_mas_larga(["lagarto", "lagarto", "lagarto", "lagarto", "perro", "gato", "perro", "gato", "perro", "gato"]))