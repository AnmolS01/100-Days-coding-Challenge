class Solution:
    # Function to serialize a tree and return an array.
    def serialize(self, root):
        if root is None:
            return []

        a = []

        def inOrder(root):
            if root:
                inOrder(root.left)
                a.append(root.data)
                inOrder(root.right)

        inOrder(root)
        return a

    # Function to deserialize an array and construct the tree.
    def deSerialize(self, a):
        def constructTree(a):
            if not a:
                return None

            mid = len(a) // 2
            root = Node(a[mid])

            root.left = constructTree(a[:mid])
            root.right = constructTree(a[mid + 1:])
            
            return root

        return constructTree(a)
