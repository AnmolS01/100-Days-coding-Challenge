# Problem Statement: Minimum element in BST
# Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

# Example 1:

# Input:
#            5
#          /    \
#         4      6
#        /        \
#       3          7
#      /
#     1
# Output: 1


class Solution:
    def minValue(self, root):
        if not root:
            return -1
        
        while root.left:
            root = root.left
        return root.data
