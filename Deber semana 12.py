# Definir la matriz 3D de temperaturas
temperaturas = [
    # Semana 1
    [
        # Ciudad 1 (Portoviejo)
        [
            25, 26, 28, 29, 30, 31, 30  # Temperaturas de lunes a domingo
        ],
        # Ciudad 2 (Quito)
        [
            18, 17, 18, 19, 20, 21, 20  # Temperaturas de lunes a domingo
        ],
        # Ciudad 3 (El Coca)
        [
            30, 31, 32, 32, 33, 34, 33  # Temperaturas de lunes a domingo
        ]
    ],
    # Semana 2
    [
        # Ciudad 1 (Portoviejo)
        [
            26, 27, 28, 29, 30, 31, 32  # Temperaturas de lunes a domingo
        ],
        # Ciudad 2 (Quito)
        [
            17, 18, 19, 20, 21, 22, 23  # Temperaturas de lunes a domingo
        ],
        # Ciudad 3 (El Coca)
        [
            31, 32, 33, 34, 35, 36, 37  # Temperaturas de lunes a domingo
        ]
    ],
    # Semana 3
    [
        # Ciudad 1 (Portoviejo)
        [
            27, 28, 29, 30, 31, 32, 33  # Temperaturas de lunes a domingo
        ],
        # Ciudad 2 (Quito)
        [
            18, 19, 20, 21, 22, 23, 24  # Temperaturas de lunes a domingo
        ],
        # Ciudad 3 (El Coca)
        [
            32, 33, 34, 35, 36, 37, 38  # Temperaturas de lunes a domingo
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad por cada semana
for semana, temp_semana in enumerate(temperaturas, start=1):
    print(f"Semana {semana}:")
    for ciudad, temp_ciudad in enumerate(temp_semana):
        promedio = sum(temp_ciudad) / len(temp_ciudad)
        print(f"  Ciudad {ciudad + 1}: Promedio de temperaturas = {promedio:.2f} °C")