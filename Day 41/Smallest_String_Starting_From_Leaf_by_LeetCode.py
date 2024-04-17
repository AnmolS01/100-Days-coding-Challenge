class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = None
        def inorder(node, current_str):
            if not node:
                return
            current_str = chr(node.val + ord('a')) + current_str
            if not node.left and not node.right:  # Leaf node
                nonlocal smallest
                if not smallest or current_str < smallest:
                    smallest = current_str
            inorder(node.left, current_str)
            inorder(node.right, current_str)
        inorder(root, '')
        return smallest
