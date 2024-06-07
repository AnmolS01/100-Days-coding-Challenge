class Solution:
    # Complete this function
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        # Step 1: Initialize frequency array
        freq = [0] * (maxx + 2)
        
        # Step 2: Populate the frequency array
        for i in range(n):
            freq[l[i]] += 1
            if r[i] + 1 <= maxx:
                freq[r[i] + 1] -= 1
        
        # Step 3: Calculate prefix sum
        max_count = 0
        max_occurring = 0
        current_count = 0
        
        for i in range(maxx + 1):
            current_count += freq[i]
            if current_count > max_count:
                max_count = current_count
                max_occurring = i
        
        return max_occurring
