def reverseLevelOrder(root):
    # code here
    if not root:
        return []

    result = []
    queue = [root] # this will contains all the root in tree.

    while queue:
        node = queue.pop(0)
        result.append(node.data)

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    return result[::-1]
