class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        result = [0] * n
        
        skip = False
        i = 0  # deck index
        j = 0  # result index
        
        deck.sort()
        
        while i < n:
            if result[j] == 0:  # if slot is empty
                if not skip:
                    result[j] = deck[i]
                    i += 1
                skip = not skip  # alternate
                
            j = (j + 1) % n
            
        return result
