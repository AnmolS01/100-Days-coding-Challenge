# Problem Statement: 143. Reorder List
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:

# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        mid = self.middle(head)
        second_half = mid.next
        mid.next = None
        second_half = self.reverse_linked_list(second_half)
        self.merge(head, second_half)
        
    def middle(self, node):
        slow = node
        fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse_linked_list(self, node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def merge(self, list1, list2):
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            
            list1.next = list2
            list1 = temp1
            
            list2.next = list1
            list2 = temp2
        
