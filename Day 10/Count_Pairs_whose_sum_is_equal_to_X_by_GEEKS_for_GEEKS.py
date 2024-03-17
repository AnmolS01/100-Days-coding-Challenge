# Q: Count Pairs whose sum is equal to X
# Given two linked list head1 and head2 with distinct elements, determine the count of all distinct pairs from both lists whose sum is equal to the given value x.

# Note: A valid pair would be in the form (x, y) where x is from first linked list and y is from second linked list.

# Example 1:

# Input:
# head1 = 1->2->3->4->5->6
# head2 = 11->12->13
# x = 15
# Output: 3
# Explanation: There are total 3 pairs whose sum is 15 : (4,11) , (3,12) and (2,13)
# Example 2:

# Input:
# head1 = 7->5->1->3
# head2 = 3->5->2->8
# x = 10
# Output: 2
# Explanation: There are total 2 pairs whose sum is 10 : (7,3) and (5,5)



class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        # This is because we do not have to traverse the linked list 
        # again as not even possible to do in O(n) 
        unique_values = set()
        a = head1
        while a:
            unique_values.add(a.data)
            a = a.next
    
        count = 0
        b = head2
        while b:
            answer = x - b.data
            if answer in unique_values:
                count += 1
            b = b.next
    
        return count
        
        # below approach takes time complexity=O(n^2)
        # a = []
        # ptr1 = head1
        # ptr2 = head2

        # for i in range(n1):
        #     ptr2 = head2
        #     for j in range(n2):
        #         if ptr1.data + ptr2.data == x:
        #             a.append((ptr1.data, ptr2.data))
        #             break
        #         ptr2 = ptr2.next
        #     ptr1 = ptr1.next

        # return len(a)
