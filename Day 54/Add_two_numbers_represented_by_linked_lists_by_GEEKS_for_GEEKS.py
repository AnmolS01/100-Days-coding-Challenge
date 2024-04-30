class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        
        def convert_to_integer(head):
            num = 0
            current = head
            while current:
                num = (num * 10) + current.data
                current = current.next
            return num
        
        nums1 = convert_to_integer(num1)
        nums2 = convert_to_integer(num2)
        sums = nums1 + nums2
        
        if sums == 0:
            return Node(0)
 
        dummyNode = Node(0)
        current = dummyNode
        
        while sums:
            Remainder = sums % 10
            current.next = Node(Remainder)
            current = current.next
            sums //= 10
        
        def reverseList(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
            
        return reverseList(dummyNode.next)
