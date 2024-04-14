# Problem Statement: 404. Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# _____________________________________________________________________CODE IS HERE_________________________________________________________________________

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sums = 0
        def preOrder(root, is_left):
            nonlocal sums
            if not root:
                return
            if not root.left and not root.right and is_left:
                sums += root.val
                return
            preOrder(root.left, True)
            preOrder(root.right, False)
            
        preOrder(root, False)
        return sums
