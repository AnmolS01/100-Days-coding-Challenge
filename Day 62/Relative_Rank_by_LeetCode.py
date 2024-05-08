# Problem Statement : 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score:
            return []

        n = len(score)
        rank = ['Gold Medal','Silver Medal','Bronze Medal']
        ranks = [0]*n
        for i in range (n):
            max_index = score.index(max(score))
            if i < 3:
                ranks[max_index] = rank.pop(0)
            else:
                ranks[max_index] = str(i+1)
            score[max_index] = -1
        return ranks
