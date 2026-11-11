from collections import deque

labels = ["P", "A", "S", "G", "A", "U", "E"]
adj = [[] for _ in range(len(labels))]


def add_edge(u, v):
    adj[u].append(v)
    adj[v].append(u)


def bfs(start):
    visited = [False] * len(labels)
    queue = deque()
    result = []

    visited[start] = True
    queue.append(start)

    while queue:
        current = queue.popleft()
        result.append(labels[current])

        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    print("BFS: " + " - ".join(result))


def dfs(current, visited, result):
    visited[current] = True
    result.append(labels[current])

    for neighbor in adj[current]:
        if not visited[neighbor]:
            dfs(neighbor, visited, result)


add_edge(0, 1)
add_edge(0, 2)
add_edge(0, 3)
add_edge(1, 4)
add_edge(2, 3)
add_edge(2, 5)
add_edge(3, 6)
add_edge(4, 5)

print("Graph Traversal (PASAGUE)")
bfs(0)
dfs_result = []
dfs(0, [False] * len(labels), dfs_result)
print("DFS: " + " - ".join(dfs_result))
