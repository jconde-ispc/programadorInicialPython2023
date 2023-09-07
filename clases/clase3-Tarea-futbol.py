# Datos de entrada
partidosGanados = int(input("Ingrese la cantidad de partidos ganados del equipo: "))
pe = int(input("Ingrese la cantidad de partidos empatados del equipo: "))
partidosPerdidos = int(input("Ingrese la cantidad de partidos perdidos del equipo: "))

# Cálculos necesarios para llegar al resultado
puntosEquipo = (partidosGanados * 3) + (pe * 1) + (partidosPerdidos * 0)

# Resultado
print("El equipo tiene", puntosEquipo, "puntos hasta el momento, luego de jugar",
                         partidosGanados + pe + partidosPerdidos, "partidos")