# Problem Statement: 2073. Time Needed to Buy Tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        countSeconds = 0
        while tickets and tickets[k] != 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    countSeconds += 1
                    if i == k and tickets[i] == 0:
                        return countSeconds
            # print(tickets)
        return countSeconds
