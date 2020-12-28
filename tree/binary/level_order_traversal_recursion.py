class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def height(node):
    if not node:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight < rheight:
            return rheight + 1
        else:
            return lheight + 1


def print_at_level(node, level):
    if not node:
        return
    if level == 1:
        print(node.data)
    print_at_level(node.left, level - 1)
    print_at_level(node.right, level - 1)


def levelOrder(root):
    h = height(root)
    for l in range(1, h + 1):
        print_at_level(root, l)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
levelOrder(root)