# deep-first-search

def dfs(graph, root, visited):
    visited.append(root) 
    for neighbor in graph[root]:
        if neighbor not in visited:
            visited = dfs(graph, neighbor, visited)
    return visited

graph = [[2,1,3], [0], [0,4], [0,2], [2]]
print(dfs(graph, 0, []))
