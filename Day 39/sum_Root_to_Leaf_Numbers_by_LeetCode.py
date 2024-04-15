# Problem Statement : 129. Sum Root to Leaf Numbers

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preOrder(root, string=''):
            if not root:
                return 0
            string += str(root.val)
            if not root.left and not root.right:
                return int(string)
            return preOrder(root.left, string) + preOrder(root.right, string)
        
        return preOrder(root)
