from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
  
        tips = [(arr[i] - brr[i], arr[i], brr[i]) for i in range(n)]
        
        tips.sort(key=lambda x: abs(x[0]), reverse=True)
        
        countA, countB = 0, 0
        total_tips = 0

        for tip_diff, tipA, tipB in tips:
            if (tipA >= tipB and countA < x) or countB >= y:
                total_tips += tipA
                countA += 1
            else:
                total_tips += tipB
                countB += 1
        
        return total_tips
