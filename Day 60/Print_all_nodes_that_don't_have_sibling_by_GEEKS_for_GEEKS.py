def noSibling(root):
    if root is None:
        return []

    result = []

    def dfs(node):
        if node is None:
            return

        if (node.left and not node.right):
            result.append(node.left.data)
        elif (node.right and not node.left):
            result.append(node.right.data)

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    if not result:
        return [-1]
    return sorted(result)
