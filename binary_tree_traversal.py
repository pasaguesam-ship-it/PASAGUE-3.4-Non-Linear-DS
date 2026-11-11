from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    print("BFS: " + " - ".join(result))


def dfs(node, result):
    if node is None:
        return
    result.append(node.data)
    dfs(node.left, result)
    dfs(node.right, result)


root = Node("P")
root.left = Node("A")
root.right = Node("S")
root.left.left = Node("A")
root.left.right = Node("G")
root.right.left = Node("U")
root.right.right = Node("E")

print("Binary Tree Traversal (PASAGUE)")
bfs(root)
dfs_result = []
dfs(root, dfs_result)
print("DFS: " + " - ".join(dfs_result))
