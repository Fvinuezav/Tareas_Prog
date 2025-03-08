# Matriz 3 dimensiones
ciudades = ["Guayaquil", "Quito", "Nueva Loja"]
dias_sem = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Temperaturas de ciudades, semana y días
temp_ciudad = {
    "Guayaquil": [
        [30, 32, 31, 29, 28, 27, 30],  # Semana 1
        [31, 30, 32, 33, 29, 28, 30],  # Semana 2
        [32, 31, 30, 29, 30, 31, 28],  # Semana 3
        [30, 29, 28, 32, 31, 30, 29]   # Semana 4
    ],
    "Quito": [
        [20, 21, 19, 18, 22, 23, 20],  # Semana 1
        [21, 20, 19, 22, 23, 21, 20],  # Semana 2
        [22, 21, 20, 19, 18, 21, 22],  # Semana 3
        [20, 22, 21, 19, 18, 20, 21]   # Semana 4
    ],
    "Nueva Loja": [
        [25, 26, 27, 28, 29, 30, 25],  # Semana 1
        [26, 25, 27, 28, 30, 29, 26],  # Semana 2
        [27, 28, 29, 26, 25, 27, 28],  # Semana 3
        [28, 29, 30, 27, 26, 28, 29]   # Semana 4
    ]
}

# Inicializamos matriz
temperaturas = []
for ciudad in ciudades:
    ciudad_temp = []
    for semana in range(semanas):
        semana_temp = temp_ciudad[ciudad][semana]
        ciudad_temp.append(semana_temp)
    temperaturas.append(ciudad_temp)

# promedio de temperaturas
for ciudad in range(len(ciudades)):
    print(f"Promedio de temperaturas para {ciudades[ciudad]}:")
    for semana in range(semanas):
        suma_temperaturas = sum(temperaturas[ciudad][semana])
        promedio = suma_temperaturas / len(dias_sem)
        print(f"  Semana {semana + 1}: {promedio:.2f} grados")
    print()