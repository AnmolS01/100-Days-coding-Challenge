# problem statement: Sum of nodes on the longest path from root to leaf node
class Solution:
    def __init__(self):
        self.max_sum = 0
        self.max_length = 0
        
    def sumOfLongRootToLeafPath(self, root):
        if not root:
            return 0
        
        def height_of_tree(root, current_height, sums):
            if not root:
                return
            
            if not root.left and not root.right:
                if current_height > self.max_length:
                    self.max_length = current_height
                    self.max_sum = sums + root.data
                elif current_height == self.max_length:
                    self.max_sum = max(self.max_sum, sums + root.data)
                return
            
            height_of_tree(root.left, current_height + 1, sums + root.data)
            height_of_tree(root.right, current_height + 1, sums + root.data)
        
        height_of_tree(root, 1, 0)
        return self.max_sum
