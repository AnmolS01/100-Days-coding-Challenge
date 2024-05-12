class Solution:
    def minSteps(self, d):
        if d <= 0:
            return 0
        if d == 1:
            return 1
    
        steps = 0
        total_steps = 0
    
        while total_steps < d or (total_steps - d) % 2 != 0:
            steps += 1
            total_steps += steps
    
        return steps
