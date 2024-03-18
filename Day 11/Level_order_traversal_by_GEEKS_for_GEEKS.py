# Given a root of a binary tree with n nodes, find its level order traversal.
# Level order traversal of a tree is breadth-first traversal for the tree.

# Example 1:

# Input:
#     1
#   /   \ 
#  3     2
# Output:
# 1 3 2
# Example 2:

# Input:
#         10
#      /      \
#     20       30
#   /   \
#  40   60
# Output:
# 10 20 30 40 60

#_________________________________________________________CODE IS HERE_____________________________________________________________

class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        # Code here
        if root is None:
            return []

        result = []
        queue = [root] #contains only root element
        while queue:
            node = queue.pop(0)
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
