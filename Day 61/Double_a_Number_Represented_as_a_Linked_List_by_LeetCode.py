# Problem Statement: 2816. Double a Number Represented as a Linked List

#  1. first Approach

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (head.val == 0 and not head.next):
            return head

        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        n = len(result)

        carry = 0
        for i in range(n-1,-1,-1):
            result[i] = result[i] * 2 + carry
            carry = result[i] // 10
            result[i] %= 10
        if carry:
            result.insert(0, carry)

        dummyHead = ListNode()
        current = dummyHead
        for val in result:
            current.next = ListNode(val)
            current = current.next
            
        return dummyHead.next


# second Approach

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0 and head.next is None:
            return ListNode(0)
        result = 0
        current = head
        while current:
            result = result * 10 + current.val 
            current = current.next
        result *= 2
        arr = []
        while result:
            unitValue = result % 10
            arr.append(unitValue)
            result = result // 10 

        dummyHead = ListNode()
        current = dummyHead
        while arr:
            current.next = ListNode(arr.pop())
            current = current.next
        return dummyHead.next
