# Encontrar el elemento que cubra más casos que no han sido cubiertos hasta el momento
# Repetir hasta que no haya espacio o se cubran todos los casos

statesNeeded = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])    # Estados que se deben cubrir

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

finalStations = set()   # Estaciones que se usarán al final

while statesNeeded:
    bestStation = None
    statesCovered = set()
    for station, statesForStation in stations.items():  # Recorre cada estación
        covered = statesNeeded & statesForStation   # Elige los estados que aún no están cubiertos pero que cubre esta estación
        if len(covered) > len(statesCovered):   # Elige la estación que cubre más estados
            bestStation = station
            statesCovered = covered
    finalStations.add(bestStation)
    statesNeeded -= statesCovered

print(finalStations)