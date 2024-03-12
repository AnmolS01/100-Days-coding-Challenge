# problem Statement: Remove zero sum consecutive by leetcode in python

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dictionary = {}
        sums = 0

        # here i added duplicate node from my side at the 
        #initial position so that when i delete nodes i am able to join the remaining nodes
        duplicate_head = ListNode(0, head) 

        temp = duplicate_head 
        while temp != None:
            sums = sums + temp.val
            dictionary[sums] = temp
            temp = temp.next

        sums = 0
        temp = duplicate_head
        while temp != None:
            sums += temp.val
            temp.next = dictionary[sums].next
            temp = temp.next

        #it will return the list from original head 
        #beacause initiall i added duplicate node just before the original head
        
        return duplicate_head.next

 
