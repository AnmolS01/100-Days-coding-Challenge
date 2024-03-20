#problem Statement: 1669. Merge In Between Linked Lists
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        x=list1
        y=list2
        while b:
            x=x.next
            b-=1
        while y.next:
            y=y.next
        y.next=x.next
        x=list1
        while a-1:
            x=x.next
            a-=1
        x.next=list2
        return list1
