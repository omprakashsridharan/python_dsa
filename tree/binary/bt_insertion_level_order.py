class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def levelOrderInsert(root, key):
    if not root:
        return
    q = []
    q.append(root)
    inserted = False
    while len(q) > 0:
        print(q[0].data)
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        else:
            if not inserted:
                node.left = Node(key)
                inserted = True
                q.append(node.left)
        if node.right:
            q.append(node.right)
        else:
            if not inserted:
                node.right = Node(key)
                inserted = True
                q.append(node.right)


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


root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.right.left = Node(15)
root.right.right = Node(8)
levelOrder(root)
levelOrderInsert(root, 12)
levelOrder(root)