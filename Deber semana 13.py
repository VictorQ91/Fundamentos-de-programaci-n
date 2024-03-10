def temperatura_promedio_ciudad(datos_temperaturas):
    temperaturas_promedio_ciudad = {}

    for ciudad, temperaturas_semanales in datos_temperaturas.items():
        total_temperaturas = 0
        contador = 0
        for semana in temperaturas_semanales:
            for temperatura in semana:
                total_temperaturas += temperatura
                contador += 1
        promedio_ciudad = total_temperaturas / contador
        temperaturas_promedio_ciudad[ciudad] = promedio_ciudad

    return temperaturas_promedio_ciudad

# Datos de temperaturas
datos_temperaturas = {
    'Portoviejo': [
        [25, 26, 27, 28, 29, 30, 31],
        [26, 27, 28, 29, 30, 31, 32],
        [27, 28, 29, 30, 31, 32, 33],
        [28, 29, 30, 31, 32, 33, 34]
    ],
    'Quito': [
        [20, 21, 22, 23, 24, 25, 26],
        [21, 22, 23, 24, 25, 26, 27],
        [22, 23, 24, 25, 26, 27, 28],
        [23, 24, 25, 26, 27, 28, 29]
    ],
    'El Coca': [
        [30, 31, 32, 33, 34, 35, 36],
        [31, 32, 33, 34, 35, 36, 37],
        [32, 33, 34, 35, 36, 37, 38],
        [33, 34, 35, 36, 37, 38, 39]
    ]
}

# Calcular temperatura promedio
resultado = temperatura_promedio_ciudad(datos_temperaturas)

# Mostrar resultado
print("Temperatura promedio por ciudad:")
for ciudad, promedio in resultado.items():
    print(f"{ciudad}: {promedio}")