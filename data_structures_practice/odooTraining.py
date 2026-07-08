# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def ArrayChallenge(arr):
    difference = arr[1] - arr[0]
    ratio = arr[1] / arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1]  != difference:
            difference = None
        if arr[i] / arr[i - 1] != ratio:
            ratio = None

    #Return th result
    if difference != None:
        return "Arithmetic"
    if ratio != None:
        return "Geometric"
    else :
        return -1

def StringChallenge(str):
    varOcg = ""
    i =0
    while i < len(str):
        if str[i] == "M":
            if len(str) > 0:
                varOcg += varOcg[-1]
            i += 1
        elif str[i] == "N":
            i += 2 #On saute le caractère suivant
        else:
            varOcg += str[i]
            i += 1
    return varOcg

from collections import deque

def GraphChallenge(strArr):
    n = int(strArr[0])

    nodes = strArr[1:n+1]
    edges = strArr[n+1:]

    # Construire le graphe (adjacency list)
    graph = {node: [] for node in nodes}

    for edge in edges:
        a, b = edge.split("-")
        graph[a].append(b)
        graph[b].append(a)

    start = nodes[0]
    end = nodes[-1]

    # BFS
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return "-".join(path)

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)

    return -1

if __name__ == '__main__':
    """
    Exercice Array :  
    print(ArrayChallenge([2,4,6,8])) # Output : Arithmetic
    print(ArrayChallenge([2, 6,18,54])) # Output : Geometric
    print(ArrayChallenge([1,2,3,4])) # Output : Arithmetic
    print(ArrayChallenge([1,4,16,64])) # Output : Geometric
    print(ArrayChallenge([1,1,1,1])) #Output : -1 (no pattern)
    """

    """
    Exercice String : 
    
    print(StringChallenge("abcNdgM"))
    print(StringChallenge("yMddN"))
    print(StringChallenge("MMyyy"))
    """


    """
    Exercice SQL : 
    Voir GoogleDoc
    """


    """
    Exercise Graph :
    """
    print(GraphChallenge(["4", "A", "B", "C", "D", "A-B", "B-D", "B-C", "C-D"]))
    # A-B-D

    print(GraphChallenge(["7", "A", "B", "C", "D", "E", "F", "G",
                          "A-B", "A-E", "B-C", "C-D", "D-F", "E-D", "F-G"]))
    # A-E-D-F-G
