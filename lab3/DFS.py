from lab2.stack import Stack 

def DFS(graph, s):
    stack1 = Stack()
    visited = set()
    stack1 = [s]

    while stack1:
        vertex = stack1.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            neighbors = graph[vertex]
            stack1.extend(neighbors)