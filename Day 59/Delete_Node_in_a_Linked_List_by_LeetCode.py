# Problem Statement : 237. Delete Node in a Linked List

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node:
            node.val = node.next.val
            node.next = node.next.next
