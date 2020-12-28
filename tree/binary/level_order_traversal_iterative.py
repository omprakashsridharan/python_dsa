class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def levelOrder(root):
    if not root:
        return
    q = []
    q.append(root)
    while len(q) > 0:
        print(q[0].data)
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
levelOrder(root)