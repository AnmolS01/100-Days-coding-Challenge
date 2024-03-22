#problem Statement : check if linked list bis palindromic or not

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=[]
        x=head
        while x:
            a.append(x.val)
            x=x.next
        a=list(reversed(a))
        b=[]
        y=head
        while y:
            b.append(y.val)
            y=y.next
        if a==b:
            return True
        else:
            False
