# Graph representation
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Representation de los costos de los nodos
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Representación de los padres de cada nodo
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Processed nodes
processed = []

def dijkestra():
    node = findLowestCostNode(costs)    # Encontrar el nodo con costo más bajo sin procesar
    while node is not None: # Mientras existan nodos por procesar continua
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # Recorre los vecinos de este nodo
            newCost = cost + neighbors[n]
            if costs[n] > newCost:  # Valida si es más barato llegar a este vecino por medio de este nodo
                costs[n] = newCost  # Actualiza el costo para llegar a este nodo
                parents[n] = node   # Este nodo se convierte en el padre de este vecino
        processed.append(node)  # Marca este nodo como procesado
        node = findLowestCostNode(costs)    #   Encuentra el siguiente nodo para procesar y continua


def findLowestCostNode(costs):
    lowestCost = float("inf")
    lowestCostNode = None
    for node in costs:  # Recorre todos los nodos
        cost = costs[node]
        if cost < lowestCost and node not in processed: # Valida si es el nodo con el costo más bajo y sin procesar
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode # Retorna el nodo con costo más bajo

dijkestra()
print(costs, parents)
# Usar Bellman-Ford para grafos con pesos negativos