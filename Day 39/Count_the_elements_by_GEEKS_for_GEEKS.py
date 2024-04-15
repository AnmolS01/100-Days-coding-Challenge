# Problem Statement:  Count the elements

class Solution:
    def countElements(self, a, b, n, query, q):
        ans = []
        b.sort()
        for i in query:
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if b[mid] <= a[i]:
                    left = mid + 1
                else:
                    right = mid
            ans.append(left)
        return ans
