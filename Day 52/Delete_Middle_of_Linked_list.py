class Solution:
    def deleteMid(self, head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        if not head or not head.next:
            return None  
            
        current = head
        n = 0
        while current:
            n += 1
            current = current.next
        
        mid_index = n // 2
        
        prev = None
        current = head
        for i in range(mid_index):
            prev = current
            current = current.next

        if prev:
            prev.next = current.next
        
        return head
