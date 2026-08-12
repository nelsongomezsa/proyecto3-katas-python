# Proyecto 3 - Katas Python

Aquí van las katas del Proyecto 3. Todo está en un solo archivo, `katas.py`,
porque son ejercicios sueltos y no tenía sentido montar una carpeta por cada
uno.

## Cómo lo he organizado

Cada kata lleva encima, como comentario, el enunciado tal cual me lo dieron
(es lo que pide la entrega). Dentro de la función solo pongo un comentario
si hay algo que a mí me costó entender la primera vez, por ejemplo cómo
`map()` puede recorrer dos listas al mismo tiempo. El resto lo dejo sin
comentar porque el código ya se explica solo.

## Para probarlo

```
python3 katas.py
```

Se ve por consola el resultado de cada kata. Las que piden datos por teclado
(dividir dos números, pedir la edad...) las he dejado como función aparte,
sin llamarlas directamente, para que no se quede el programa esperando
input al ejecutar todo el archivo. Si quieres probar una en concreto,
descomenta la línea que hay justo debajo, tipo:

```python
# pedir_edad()  # descomentar para probarla a mano
```

## Cómo he ido avanzando

Las he resuelto por bloques, más o menos de 10 en 10, empezando por las
más básicas (map, filter, alguna excepción sencilla) e ir subiendo la
dificultad poco a poco. Al principio puse los comentarios de cada kata
como un resumen corto mío, pero luego caí en que el enunciado pide el
texto completo del ejercicio, así que lo corregí para dejarlo tal cual.

Para la kata de convertir una lista de dígitos en un número usé
`functools.reduce`, que no había usado mucho antes, así que le dediqué
un rato aparte para entender bien cómo iba acumulando el resultado. Luego
salieron varias katas seguidas con `reduce` (producto total, concatenar
palabras, diferencia total) y ya le pillé el truco más rápido.

Voy subiendo el trabajo a GitHub en commits por bloques, a medida que
termino y compruebo que el archivo corre sin errores.

## Cosas que se ven a lo largo de las katas

- Tipos de datos básicos y funciones incorporadas de Python.
- Listas, diccionarios, tuplas y sets, con sus métodos.
- Condicionales y bucles.
- Funciones normales, lambdas y una recursiva (el factorial).
- Manejo de excepciones, incluyendo una excepción propia (`ListaVaciaError`).
