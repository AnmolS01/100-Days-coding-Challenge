#problem Statement: Kth common ancestor in BST

class Solution:
    def LCA(self, root, x, y):
        if not root:
            return None
        if root.data == x or root.data == y:
            return root
        elif root.data < x and root.data < y:
            return self.LCA(root.right, x, y)
        elif root.data > x and root.data > y:
            return self.LCA(root.left, x, y)
        else:
            return root
    
    def f(self, root, lca, path):
        if root is None:
            return
        path.append(root.data)
        if root.data == lca.data:
            return
        elif root.data > lca.data:
            self.f(root.left, lca, path)
        else:
            self.f(root.right, lca, path)
    
    def kthCommonAncestor(self, root, k, x, y):
        lca = self.LCA(root, x, y)
        path = []
        self.f(root, lca, path)
        n = len(path)
        if len(path) < k:
            return -1
        return path[n - k]
