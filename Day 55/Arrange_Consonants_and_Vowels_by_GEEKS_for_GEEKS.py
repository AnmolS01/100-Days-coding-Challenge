class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        vowel = set(['a','e','i','o','u'])
        
        v = ''
        c = ''
        
        current = head
        while current:
            if current.data in vowel:
                v += current.data
            else:
                c += current.data
            current = current.next
            
        current = head
        n = len(v)
        m = len(c)
        i = 0
        j = 0
        while current:
            if i < n:
                current.data = v[i]
                current = current.next
                i += 1
            else:
                if j < m:
                    current.data = c[j] 
                    current = current.next
                    j += 1
        return head
