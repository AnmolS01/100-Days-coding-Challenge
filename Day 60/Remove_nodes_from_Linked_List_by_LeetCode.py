# Problem Statement: 2487. Remove Nodes From Linked List

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        stack = []
        current = head
    
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next
    
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None
    
        return stack[0]
