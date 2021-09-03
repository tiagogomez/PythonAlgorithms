graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


from collections import deque
def search(name):
    searchQueue = deque()   # Creo una cola 
    searchQueue += graph[name] # Agrego mis vecinos a la lista
    searched = []   # Lista de elementos donde ya se buscó

    while searchQueue: # Mientras la cola no esté vacía
        person = searchQueue.popleft()  # Saca el primer elemento de la cola
        if not person in searched:  # Valida si la persona está en la lista de elementos validados
            if personIsSeller(person):  # Comprueba si la persona es un vendedor
                print(person + " is a seller")    
                return True # Finaliza la busqueda
            else:
                searchQueue += graph[person]    # Si no es vendedor, agrega sus vecinos a la lista
                searched.append(person) # Agrega la persona en la lista de validados
    return False    # Si nadie es vendedor finaliza la busqueda

def personIsSeller(name):
    return name[-1] == "m" # Esta función valida si un nombre termina con la letra m

search("you")