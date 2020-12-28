class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inorder(root):
    current = root
    while current:
        if current.left is None:
            yield current.data
            current = current.right
        else:
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right
            if not pre.right:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                yield current.data
                current = current.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
for v in inorder(root):
    print(v)