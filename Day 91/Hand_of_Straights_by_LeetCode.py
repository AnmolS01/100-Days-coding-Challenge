# 846. Hand of Straights

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        unique_cards = sorted(count.keys())
    
        for card in unique_cards:
            if count[card] > 0:
                start_count = count[card]
                for i in range(groupSize):
                    if count[card + i] < start_count:
                        return False
                    count[card + i] -= start_count
                
        return True
