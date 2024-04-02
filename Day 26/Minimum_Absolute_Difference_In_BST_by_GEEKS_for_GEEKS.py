# Problem Statement: Minimum Absolute Difference In BST

class Solution:
    def absolute_diff(self, root):
        # Your code here
        inorder_list = []

        def inorderTraversal(node): # This function returns sorted list 
            if not node:
                return
            inorderTraversal(node.left)
            inorder_list.append(node.data)
            inorderTraversal(node.right)
        inorderTraversal(root)

        min_length = float('inf')

        for i in range(len(inorder_list) - 1):
            if inorder_list[i + 1] - inorder_list[i] < min_length:
                min_length = inorder_list[i + 1] - inorder_list[i]

        return min_length
