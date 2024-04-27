class Solution:
    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first
        
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            if first.next:
                first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            if second.next:
                second.next.prev = second
            second.prev = None
            return second

    def split(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        return temp

    def sortDoubly(self, head):
        if not head or not head.next:
            return head

        secondHalf = self.split(head)

        head = self.sortDoubly(head)
        secondHalf = self.sortDoubly(secondHalf)

        return self.merge(head, secondHalf)
