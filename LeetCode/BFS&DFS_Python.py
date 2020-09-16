#BFS
graph = {
    "A" : ["B", "C"],
    "B" : ["A", "C", "D"],
    "C" : ["A", "B", "D", "E"],
    "D" : ["B", "C", "E", "F"],
    "E" : ["C", "D"],
    "F" : ["D"]
}

def BFS(graph, startNode):
    queue = []
    queue.append(startNode)
    seen = set()
    seen.add(startNode)

    while (len(queue) > 0):
        vertex = queue.pop(0)
        print(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)

BFS(graph, "A")

#DFS, by only change the pop(),which is poping the last one, to pop(0), which is poping the first one.
graph = {
    "A" : ["B", "C"],
    "B" : ["A", "C", "D"],
    "C" : ["A", "B", "D", "E"],
    "D" : ["B", "C", "E", "F"],
    "E" : ["C", "D"],
    "F" : ["D"]
}

def DFS(graph, startNode):
    stack = []
    stack.append(startNode)
    seen = set()
    seen.add(startNode)

    while (len(stack) > 0):
        vertex = stack.pop()
        print(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)

DFS(graph, "A")
