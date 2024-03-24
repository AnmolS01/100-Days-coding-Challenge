# Insert an Element at the Bottom of a Stack

# You are given a stack st of n integers and an element x. You have to insert x at the bottom of the given stack. 
# Note: Everywhere in this problem, the bottommost element of the stack is shown first while priniting the stack.

# Example 1:

# Input:
# n = 5
# x = 2
# st = {4,3,2,1,8}
# Output:
# {2,4,3,2,1,8}
# Explanation:
# After insertion of 2, the final stack will be {2,4,3,2,1,8}.

# ________________________________________________________CODE IS HERE_____________________________________________________________

class Solution:
    def insertAtBottom(self,st,x):
        # code here
        new_stack = []
        new_stack.append(x)
        for val in st:
            new_stack.append(val)
        return new_stack
