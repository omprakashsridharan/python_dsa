def get_level_order(root):
    if not root:
        return []
    res = []
    q = []
    q.append(root)
    while len(q) > 0:
        res.append(q[0].data)
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


def deletionBT(root, key):
    """
    root: root of tree
    key:  key to be deleted
    return: root after deleting
    """
    if not root:
        return
    lot = get_level_order(root)
    if len(lot) > 0:
        rightmost_node = lot[len(lot) - 1]
        q = []
        q.append(root)
        while len(q) > 0:
            if q[0] and q[0].data == key:
                q[0].data = rightmost_node
            node = q.pop(0)
            if node and node.left:
                if node.left.data == rightmost_node:
                    node.left = None
                q.append(node.left)
            if node and node.right:
                if node.right.data == rightmost_node:
                    node.right = None
                q.append(node.right)