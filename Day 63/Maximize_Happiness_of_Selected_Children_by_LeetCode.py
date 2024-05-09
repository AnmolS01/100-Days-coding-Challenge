# problem Statement : 3075. Maximize Happiness of Selected Children

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        if not happiness or k == 0:
            return 0
            
        maxHappiness = 0
        decrement = 0
        happiness.sort()

        for i in range (k):
            if (happiness[-1] - decrement) < 0:
                break
            elif (happiness[-1] - decrement) > 0:
                maxHappiness += happiness.pop() - decrement
                decrement += 1
            else:
                maxHappiness += 0
        return maxHappiness 
