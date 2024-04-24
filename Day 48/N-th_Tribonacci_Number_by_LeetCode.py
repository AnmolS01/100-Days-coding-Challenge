# Problem Statement: 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if (n==1 or n==2):
            return 1
        T0, T1, T2 = 0, 1, 1
        for i in range (3,n+1):
            T = T0 + T1 + T2
            T0, T1, T2 = T1, T2, T
        return T
