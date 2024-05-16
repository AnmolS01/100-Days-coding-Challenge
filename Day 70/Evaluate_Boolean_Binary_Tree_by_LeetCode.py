# 2331. Evaluate Boolean Binary Tree

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return root.val

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        return left and right if root.val == 3 else left or right
