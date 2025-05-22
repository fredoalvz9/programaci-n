def calcular_ahorro(consumo_anterior, consumo_actual, tipo):
    """Calcula el ahorro o aumento en el consumo de electricidad, agua o personal."""
    ahorro = consumo_anterior - consumo_actual

    if ahorro < 0:
        print(f"No hubo ahorro en {tipo}. El consumo aumentó en {-ahorro:.2f}.")
    elif ahorro > 0:
        print(f"Se ahorró en {tipo}: {ahorro:.2f}.")
    else:
        print(f"El consumo de {tipo} se mantuvo igual, sin ahorro ni aumento.")

def calcular_ahorro_personal(Cantidad_PersonalMesPasado, Personal_añadido, sueldo_por_persona):
    """Calcula el ahorro en costo de personal de mantenimiento."""
    Total_PersonalActual = Personal_añadido  # Ahora considera solo el personal actual
    diferencia_personal = Cantidad_PersonalMesPasado - Total_PersonalActual

    if Total_PersonalActual > Cantidad_PersonalMesPasado:
        print("No hay ahorro en costos de personal de mantenimiento, debido al aumento de personal.")
    elif Total_PersonalActual == Cantidad_PersonalMesPasado:
        print("No hay ahorro en costos de personal de mantenimiento, es el mismo del mes pasado.")
    else:
        ahorro_mensual = diferencia_personal * sueldo_por_persona
        print(f"Se logró un ahorro en costos de personal de mantenimiento de: {ahorro_mensual:.2f}.")

# Capturar entradas y calcular ahorros automáticamente al ejecutar el script
e_anterior = float(input("Ingrese el consumo eléctrico del mes anterior (kWh): "))
e_actual = float(input("Ingrese el consumo eléctrico del mes actual (kWh): "))
calcular_ahorro(e_anterior, e_actual, "electricidad")

agua_anterior = float(input("Ingrese el consumo de agua del mes anterior (m³): "))
agua_actual = float(input("Ingrese el consumo de agua del mes actual (m³): "))
calcular_ahorro(agua_anterior, agua_actual, "agua")

Cantidad_PersonalMesPasado = int(input("Ingrese la cantidad de personal de mantenimiento del mes anterior: "))
Personal_añadido = int(input("Ingrese la cantidad actual de personal de mantenimiento: "))
sueldo_por_persona = float(input("Ingrese el sueldo mensual por persona: "))
calcular_ahorro_personal(Cantidad_PersonalMesPasado, Personal_añadido, sueldo_por_persona)
