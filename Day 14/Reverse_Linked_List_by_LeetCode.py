# Problem Statement: 206. Reverse Linked List

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x = head
        a = []
        while x:
            a.append(x.val)
            x = x.next
        a.reverse()
        x = head
        for val in a:
            x.val = val
            x=x.next
        return head
