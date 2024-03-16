# problem Statement: Delete without head pointer

class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,del_node):
        
        x = del_node
        while x.next:
            x.data = x.next.data
            if x.next.next is None:
                x.next = None
                return
            x = x.next
