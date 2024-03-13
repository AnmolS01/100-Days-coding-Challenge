# problem Statement: find the pivot integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        mid=n//2+1
        tsum=n*(n+1)//2
        while mid<n-1:
            a=mid*(mid+1)//2
            b=tsum-a+mid
            if a==b:
                return mid
            mid +=1
        return -1
        
