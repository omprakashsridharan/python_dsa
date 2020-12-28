class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inorder(root):
    current = root
    stack = []
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder(root)