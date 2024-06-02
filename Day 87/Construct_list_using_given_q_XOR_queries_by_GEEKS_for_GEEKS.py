from typing import List

class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
        s = [0]
        xor = 0
        
        for query in queries:
            if query[0] == 0:
                s.append(query[1] ^ xor)
                
            elif query[0] == 1:
                xor ^= query[1]
        s = [x ^ xor for x in s]
        s.sort()
        return s
        
        
