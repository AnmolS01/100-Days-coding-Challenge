# Given a binary tree with n nodes. Find the zig-zag level order traversal of the binary tree.

# Example 1:

# Input:
#         1
#       /   \
#      2    3
#     / \    /   \
#    4   5 6   7
# Output:
# 1 3 2 4 5 6 7
# Example 2:

# Input:
#            7
#         /     \
#        9      7
#      /  \      /   
#     8   8  6     
#    /  \
#   10  9 


# Approach: i perform level order traversal, i started my level at n=1. i.e root is level 1
# This approach ensures that nodes at odd levels are visited from left to right, while nodes at even levels are visited from right to left,
# thereby achieving the zigzag traversal pattern.

# ________________________________________________________________________________CODE IS HERE___________________________________________________________________________________________

class Solution:
    # Function to store the zigzag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        if root is None:
            return []

        result = []
        queue = [root] # CONTAINS ROOT ELEMENTS ONLY
        n = 1

        while queue:
            level_values = []
            size = len(queue)
            
            for i in range(size):
                if n % 2 != 0:
                    node = queue.pop(0)
                    level_values.append(node.data)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    level_values.append(node.data)
                    if node.right:
                        queue.insert(0, node.right)
                    if node.left:
                        queue.insert(0, node.left)
            result.extend(level_values)
            n += 1

        return result
