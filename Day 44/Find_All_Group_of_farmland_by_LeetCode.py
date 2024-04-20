class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ansList = []
        def dfs(land, i, j):
            nonlocal startX, startY, endX, endY
            
            n = len(land)
            m = len(land[0])
            # Out of bounds
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            # Visited for forest land
            if land[i][j] == 0 or land[i][j] == -1:
                return
            # Work
            endX = max(endX, i)
            endY = max(endY, j)
            land[i][j] = -1
            # Check again
            dfs(land, i - 1, j)
            dfs(land, i, j + 1)
            dfs(land, i + 1, j)
            dfs(land, i, j - 1)
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    startX = i
                    startY = j
                    endX = i
                    endY = j
                    dfs(land, i, j)
                    ansList.append([startX, startY, endX, endY])
        return ansList


