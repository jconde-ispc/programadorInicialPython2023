# Datos de entrada
nota1 = float(input("La nota de la materia 1 es: "))
nota2 = float(input("La nota de la materia 2 es: "))
nota3 = float(input("La nota de la materia 3 es: "))
nota4 = float(input("La nota de la materia 4 es: "))
nota5 = float(input("La nota de la materia 5 es: "))

# Hago los cálculos necesarios para llegar al resultado
sumaTotalNotas = nota1 + nota2 + nota3 + nota4 + nota5
#sumaTotalNotas = nota1 * 2
print("La suma total de las notas es:", sumaTotalNotas)
CANTIDAD_NOTAS = 5
print("La cantidad de notas es:", CANTIDAD_NOTAS)
promedio = sumaTotalNotas / CANTIDAD_NOTAS

# Resultado
print("El promedio de las notas es:", promedio)