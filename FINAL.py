# Creamos listas vacías
meses = []
consumos = []

# Pedimos datos para 3 meses
for i in range(3):
    mes = input(f"Ingrese el nombre del mes {i+1}: ")
    consumo = float(input(f"Ingrese el consumo de luz de {mes} en kWh: "))

    # Guardamos usando append
    meses.append(mes)
    consumos.append(consumo)

# Mostramos los resultados
print("\nResumen de consumos:")
for i in range(3):
    print(f"{meses[i]}: {consumos[i]} kWh")

promedio = sum(consumos) / len(consumos)
print(f"\nEl consumo promedio es: {promedio:.2f} kWh")    

# Encontrar mes con mayor consumo
mayor_consumo = max(consumos)
indice_mayor = consumos.index(mayor_consumo)
mes_mayor = meses[indice_mayor]

print(f"El mes donde hubo mayor consumo es: {mes_mayor}, {mayor_consumo}")    

# Encontrar mes con menor consumo
menor_consumo = min(consumos)
indice_menor = consumos.index(menor_consumo)
mes_menor = meses[indice_menor]
print(f"El mes donde hubo más menor consumo es: {mes_menor}, {menor_consumo}")
