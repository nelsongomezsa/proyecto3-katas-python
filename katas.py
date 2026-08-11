# proyecto 3: katas python
# comentarios cortos explicando qué hace cada función
# los ejercicios interactivos quedan como función, se llaman a mano si se quieren probar

from functools import reduce


# Kata 1: Escribe una función que reciba una cadena de texto como parámetro
# y devuelva un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
def contar_frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto:
        if letra == ' ':
            continue
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias


print(contar_frecuencia_letras("hola hola"))


# Kata 2: Dada una lista de números, obtén una nueva lista con el doble de
# cada valor. Usa la función map().
def duplicar_valores(numeros):
    return list(map(lambda numero: numero * 2, numeros))


print(duplicar_valores([1, 2, 3, 4]))


# Kata 3: Escribe una función que tome una lista de palabras y una palabra
# objetivo como parámetros. La función debe devolver una lista con todas
# las palabras de la lista original que contengan la palabra objetivo.
def buscar_palabras_que_contienen(palabras, objetivo):
    resultado = []
    for palabra in palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado


print(buscar_palabras_que_contienen(["casa", "casita", "perro", "gato"], "casa"))


# Kata 4: Genera una función que calcule la diferencia entre los valores de
# dos listas. Usa la función map().
def diferencia_listas(lista1, lista2):
    # map() puede recorrer dos listas a la vez, elemento a elemento
    return list(map(lambda a, b: a - b, lista1, lista2))


print(diferencia_listas([10, 20, 30], [1, 2, 3]))


# Kata 5: Escribe una función que tome una lista de números como parámetro
# y un valor opcional nota_aprobado (por defecto 5). La función debe
# calcular la media de los números en la lista y determinar si la media es
# mayor o igual que nota_aprobado. Si es así, el estado será "aprobado";
# de lo contrario, "suspenso". La función debe devolver una tupla que
# contenga la media y el estado.
def calcular_media_y_estado(numeros, nota_aprobado=5):
    media = sum(numeros) / len(numeros)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)


print(calcular_media_y_estado([4, 5, 6, 7]))


# Kata 6: Escribe una función que calcule el factorial de un número de
# manera recursiva.
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * factorial(numero - 1)


print(factorial(5))


# Kata 7: Genera una función que convierta una lista de tuplas a una lista
# de strings. Usa la función map().
def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))


print(tuplas_a_strings([(1, 2), (3, 4), (5, 6)]))


# Kata 8: Escribe un programa que pida al usuario dos números e intente
# dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir
# por cero, maneja esas excepciones de manera adecuada y muestra un mensaje
# indicando si la división fue exitosa o no.
def dividir_numeros():
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        resultado = numero1 / numero2
    except ValueError:
        print("División no exitosa: debes introducir un número válido.")
    except ZeroDivisionError:
        print("División no exitosa: no se puede dividir entre cero.")
    else:
        print(f"División exitosa. Resultado: {resultado}")


# dividir_numeros()  # descomentar para probarla a mano


# Kata 9: Escribe una función que tome una lista de nombres de mascotas
# como parámetro y devuelva una nueva lista excluyendo ciertas mascotas
# prohibidas en España. La lista de mascotas a excluir es ["Mapache",
# "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
def filtrar_mascotas_permitidas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


print(filtrar_mascotas_permitidas(["Perro", "Gato", "Tigre", "Hamster", "Oso"]))


# Kata 10: Escribe una función que reciba una lista de números y calcule su
# promedio. Si la lista está vacía, lanza una excepción personalizada y
# maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass


def calcular_promedio(numeros):
    if len(numeros) == 0:
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    return sum(numeros) / len(numeros)


try:
    print(calcular_promedio([]))
except ListaVaciaError as error:
    print(error)


# Kata 11: Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del rango
# esperado (por ejemplo, menor que 0 o mayor que 120), maneja las
# excepciones adecuadamente.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("la edad debe estar entre 0 y 120")
    except ValueError as error:
        print(f"Edad no válida: {error}")
    else:
        print(f"Edad registrada: {edad}")


# pedir_edad()  # descomentar para probarla a mano


# Kata 12: Genera una función que, al recibir una frase, devuelva una lista
# con la longitud de cada palabra. Usa la función map().
def longitudes_palabras(frase):
    return list(map(len, frase.split()))


print(longitudes_palabras("hola que tal estas"))
