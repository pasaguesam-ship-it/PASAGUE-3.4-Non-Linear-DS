class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node, result):
    if node is None:
        return
    result.append(node.data)
    preorder(node.left, result)
    preorder(node.right, result)


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.data)


root = Node("P")
root.left = Node("M")
root.right = Node("A")

root.left.left = Node("A")
root.left.right = Node("T")
root.right.left = Node("U")
root.right.right = Node("H")

root.left.left.left = Node("S")
root.left.left.right = Node("E")
root.left.right.left = Node("A")
root.left.right.right = Node("A")
root.right.left.left = Node("A")
root.right.left.right = Node("N")
root.right.right.left = Node("S")
root.right.right.right = Node("G")

print("DFS Methods in Tree (SAMANTHA PASAGUE)")

pre_result = []
preorder(root, pre_result)
print("Preorder: " + " - ".join(pre_result))

in_result = []
inorder(root, in_result)
print("Inorder: " + " - ".join(in_result))

post_result = []
postorder(root, post_result)
print("Postorder: " + " - ".join(post_result))
