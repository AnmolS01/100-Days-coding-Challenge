from collections import defaultdict
from heapq import merge

class Solution:
    def printKClosest(self, arr, n, k, x):
        mp = defaultdict(list)
        for num in arr:
            mp[abs(num - x)].append(num)
        
        ans = []
        for key in sorted(mp.keys()):
            if key == 0:
                continue
            if k == 0:
                break
            # Sort in descending order
            mp[key].sort(reverse=True)
            for num in mp[key]:
                ans.append(num)
                k -= 1
                if k == 0:
                    break
        return ans
