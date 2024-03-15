# Linked List that is Sorted Alternatingly
# You are given a Linked list of size n. The list is in alternating ascending and descending orders. Sort the given linked list in non-decreasing order.

# Example 1:

# Input:
# n = 6
# LinkedList = 1->9->2->8->3->7
# Output: 1 2 3 7 8 9
# Explanation: 
# After sorting the given list will be 1->2->3->7->8->9.
# Example 2:

# Input:
# n = 5
# LinkedList = 13->99->21->80->50
# Output: 13 21 50 80 99
# Explanation:
# After sorting the given list will be 13->21->50->80->99.


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def sort(self, h1):
        values = []
        X = h1
        while X:
            values.append(X.data)
            X = X.next
        
        values.sort()

        SH = None
        for value in values:
            if not SH:
                SH = Node(value)
                X = SH
            else:
                X.next = Node(value)
                X = X.next
        
        return SH
