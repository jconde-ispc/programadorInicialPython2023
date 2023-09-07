# Datos de entrada
altoPared = float(input("Ingrese el alto de la pared: "))
anchoPared = float(input("Ingrese el ancho de la pared: "))
costoPintorPorM2 = float(input("Ingrese el costo del metro cuadrado que cobra el pintor: "))

# Cálculos necesarios para lograr el resultado
superficiePared = altoPared * anchoPared
print("El galpón tiene un ancho de", anchoPared, "metros y un alto de", altoPared, "metros")
print("Esto hace que la superficie del galpón sea de", superficiePared, "metros cuadrados")

# Resultado
costoManoObra = superficiePared * costoPintorPorM2
print("El costo de mano de obra del pintor para pintar el galpón es de", costoManoObra)