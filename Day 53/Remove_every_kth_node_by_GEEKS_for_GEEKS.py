class Solution:
    def deleteK(self, head, k):
        #code here  
        
        if not head or k <= 1:
            return None
        
        count = 1
        current = head
        while current:
            count += 1
            if count == k:
                if current.next:
                    current.next = current.next.next
                    count = 1
            current = current.next
        return head
