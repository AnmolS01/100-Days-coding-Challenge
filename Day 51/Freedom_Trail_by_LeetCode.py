# Problem Statement: 514. Freedom Trail

class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        len_key, len_ring = len(key), len(ring)
      
        char_positions = defaultdict(list)
 
        for index, char in enumerate(ring):
            char_positions[char].append(index)

        dp = [[inf] * len_ring for _ in range(len_key)]
        for j in char_positions[key[0]]:

            dp[0][j] = min(j, len_ring - j) + 1
        for i in range(1, len_key):
            for j in char_positions[key[i]]:
                for k in char_positions[key[i - 1]]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(abs(j - k), len_ring - abs(j - k)) + 1)
        return min(dp[-1][j] for j in char_positions[key[-1]])
        
