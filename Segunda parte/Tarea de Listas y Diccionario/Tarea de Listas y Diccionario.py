# --- Problema 1: Implementar el algoritmo Iterativo Sort Intercambio
def sort_intercambio(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Ejemplo de uso de Sort Intercambio:
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
print("Lista ordenada (Intercambio):", sort_intercambio(lista))

# --- Problema 2: Implementar el algoritmo Sort Insercion
def sort_insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Ejemplo de uso de Sort Insercion:
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
print("Lista ordenada (Inserción):", sort_insercion(lista))

# --- Problema 3: Gestión de información de las olimpiadas
def Diccionarios():
    # -- Crear diccionario de paises
    DP = {
        "PE": ["PERU", "AMÉRICA"],
        "BR": ["BRASIL", "AMÉRICA"],
        "US": ["USA", "AMÉRICA"],
        "ES": ["ESPAÑA", "EUROPA"],
        "FR": ["FRANCIA", "EUROPA"],
        "GE": ["ALEMANIA", "EUROPA"],
        "NP": ["JAPÓN", "ASIA"],
        "CH": ["CHINA", "ASIA"],
        "EG": ["EGIPTO", "AFRICA"],
        "AU": ["AUSTRALIA", "OCEANÍA"],
        "NZ": ["NUEVA ZELANDA", "OCEANÍA"]
    }
    # -- Crear diccionario de Disciplinas
    DD = {
        "101": ["ATLETISMO 100 MTS", "INDIVIDUAL"],
        "102": ["ATLETISMO 400 MTS", "INDIVIDUAL"],
        "204": ["BALONCESTO", "EQUIPO"],
        "209": ["FÙTBOL", "EQUIPO"],
        "309": ["KARATE", "INDIVIDUAL"],
        "511": ["SURF", "INDIVIDUAL"]
    }
    # -- Crear diccionario de Resultados
    DR = {
        "101": ["US", "CH", "GE"],
        "102": ["US", "FR", "BR"],
        "204": ["US", "FR", "BR"],
        "209": ["BR", "ES", "US"],
        "309": ["CH", "NP", "AU"],
        "511": ["AU", "US", "BR"]
    }
    # -- Devolver resultados
    return DP, DD, DR

# --- Pregunta 1: Mostrar que tipo de medallas ha obtenido más un determinado país
def medallas_pais(pais):
    DP, DD, DR = Diccionarios()
    medallas = {"ORO": 0, "PLATA": 0, "BRONCE": 0}
    for resultados in DR.values():
        if resultados[0] == pais:
            medallas["ORO"] += 1
        if resultados[1] == pais:
            medallas["PLATA"] += 1
        if resultados[2] == pais:
            medallas["BRONCE"] += 1
    return medallas

# Ejemplo de uso de medallas_pais:
pais = "US"
medallas = medallas_pais(pais)
print(f"Medallas obtenidas por {pais}: {medallas}")

# --- Pregunta 2: Determinar que continente obtuvo más medallas de oro
def continente_con_mas_oros():
    DP, DD, DR = Diccionarios()
    oros_continente = {}
    for resultados in DR.values():
        pais_oro = resultados[0]
        continente = DP[pais_oro][1]
        if continente in oros_continente:
            oros_continente[continente] += 1
        else:
            oros_continente[continente] = 1
    continente_max = max(oros_continente, key=oros_continente.get)
    return continente_max, oros_continente[continente_max]

# Ejemplo de uso de continente_con_mas_oros:
continente, cantidad_oros = continente_con_mas_oros()
print(f"El continente con más medallas de oro es {continente} con {cantidad_oros} medallas.")
