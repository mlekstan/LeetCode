# breadth-first-

from typing import List

def bfs(graph: List[List], root: int) -> List:
    visited = []
    queue = [root]
        
    while queue:
        verticle = queue.pop(0)
        if verticle not in visited:    
            visited.append(verticle)
            for i in graph[verticle]:
                if i not in visited:     
                    queue.append(i)
        
    return visited


graph = [[2,1,3], [0], [0,4], [0,2], [2]]
print(bfs(graph, 0))