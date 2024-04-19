class Solution:
    def findMissing(self,a,b,n,m):
        hashSet = set(b)
        res = []
        for i in a:
            if i not in hashSet:
                res.append(i)
        return res
