import math

# 1.1
# def imprimir_hola_mundo():
#     print("hola mundo")

# def imprimir_hola_mundo_2():
#     return "hola mundo 2"

# imprimir_hola_mundo()

# print(imprimir_hola_mundo_2())

# 1.3
# def raizDe2():
#     return round(math.sqrt(2), 4)

# print(raizDe2())

# 2.1
# def imprimir_saludo(nombre: str):
#     print("Hola " + nombre)

# imprimir_saludo("juan")

# 2.2
# def raiz_cuadrada_de(numero: float):
#     return round(math.sqrt(numero), 5)

# print(raiz_cuadrada_de(2))

# 2.3
# def fahrenheit_a_celsius(t: float) -> float:
#     res: float = ((t - 32) * 5) / 9
#     return res

# print(fahrenheit_a_celsius(59))

# 2.4
# def imprimir_dos_veces(estribillo: str):
#     print(estribillo * 2)

# imprimir_dos_veces("hola ")

# 2.5
def es_multiplo_de(n: int, m: int) -> bool:
    if m == 0:
        return False
    return n % m == 0

# print(es_multiplo_de(10, 2))

# 2.6
def es_par(numero: int) -> bool:
    return es_multiplo_de(numero, 2)

# print(es_par(3))

# 2.7
# def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
#     pizzas: int = math.ceil((min_cant_de_porciones * comensales) / 8)
#     return pizzas

# print(cantidad_de_pizzas(6, 2))

# 3.1
# def algunos_es_0(numero1, numero2):
#     return numero1 == 0 or numero2 == 0

# print(algunos_es_0(1,0))

# 3.2
# def ambos_son_0(numero1, numero2):
#     return numero1 == 0 and numero2 == 0

# print(ambos_son_0(0,0))

# 3.3
# def es_nombre_largo(nombre: str) -> bool:
#     return len(nombre) >= 3 and len(nombre) <= 8

# print(es_nombre_largo("juan"))

# 3.4 
# def es_bisiesto(año):
#     return es_multiplo_de(año, 400)
#     return (año%4==0) and ((año%100!=0) or (año%400==0))

# print(es_bisiesto(2000))

# 4.1
# def peso_pino(altura: int) -> int:
#     if altura < 300:
#         return altura * 3
#     else:
#         return 900 + 2 * (altura - 300)

# print(peso_pino(500))

# 4.2
# def es_peso_util(peso: int) -> bool:
#     return peso >= 400 and peso <= 1000

# print(es_peso_util(500))

# 4.3
# def sirve_pino(altura: int) -> bool:
#     return es_peso_util(peso_pino(altura))

# print(sirve_pino(200))

# 5.1
# def devolver_el_doble_si_es_par(numero: int) -> int:
#     if es_par(numero):
#         return numero * 2
#     else:
#         return numero
    
# print(devolver_el_doble_si_es_par(3))

# 5.2
# def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
#     if es_par(numero):
#         return numero
#     else:
#         return numero + 1
    
# print(devolver_valor_si_es_par_sino_el_que_sigue(12))

# 5.3
# def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
#     if es_multiplo_de(numero, 3):
#         return numero * 2
#     elif es_multiplo_de(numero, 9):
#         return numero * 3
#     else:
#         return numero

# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(5))

# 5.4
# def lindo_nombre(nombre: str) -> str:
#     if len(nombre) >= 5:
#         print("Tu nombre tiene muchas letras!")
#     else:
#         print("Tu nombre tiene menos de 5 caracteres")

# lindo_nombre("juaan")

# 5.5
# def elRango(numero: int) -> str:
#     if numero < 5:
#         print("Menor a 5")
#     elif numero >= 10 and numero <= 20:
#         print("Entre 10 y 20")
#     elif numero > 20:
#         print("Mayor a 20")
#     else:
#         print("???")

# elRango(7)

# 5.6
# def laburo(genero:str,edad:int):
#     if (genero=="F"):
#         if(18<=edad<60):
#             print("Te toca trabajar")
#         else:
#             print("Andá de vacaciones")
#     elif(genero=="M"):
#         if(18<=edad<65):
#             print("Te toca trabajar")
#         else:
#             print("Andá de vacaciones")

# 6.1
# def numeros_1_10():
#     i = 1
#     while (i <= 10):
#         print(i)
#         i += 1

# numeros_1_10()

# 6.2
# def numeros_pares():
#     i = 10
#     while (i <= 40):
#         print(i)
#         i += 2

# numeros_pares()

# 6.3
# def eco():
#     i = 1
#     while (i <= 10):
#         print("eco")
#         i += 1

# eco()

# 6.4
# def cohete(i: int):
#     while (i >= 1):
#         print(i)
#         i -= 1
#     print("Despegue")

# cohete(10)

# 7
# def numeros_del_1_al_10_v2() -> None:
#     for i in range(1,11,1):
#         print(i)

# def numeros_del_10_al_40_v2() -> None:
#     for i in range(10,41,2):
#         print(i)

# def eco_v2() -> None:
#     for i in range (0,10,1):
#         print("Eco")

# def cohete_v2(numero:int) -> None:
#     for i in range (0,numero,1):
#         print(numero)
#         numero-=1
#     print("Cohete")

# def viajeEnElTiempo_v2(añoDeSalida:int,añoDeLlegada:int)->None:
#     for i in range(añoDeLlegada,añoDeSalida,1):
#         print("Viajó un año al pasado, estamos en el año "+str(añoDeSalida))
#         añoDeSalida-=1

# def conocerAAristoteles_v2(añoDeSalida:int):
#     for i in range(384,añoDeSalida,20):
#         print("Viajó 20 años al pasado, estamos en el "+str(añoDeSalida))
#         añoDeSalida-=20
#     if(añoDeSalida>=374):
#         print("Viajó 20 años al pasado, estamos en el "+str(añoDeSalida))

# 