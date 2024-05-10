class Solution:
    
    def CombinationSum2(self, arr, n, k):
        ans = []

        def dfs(s, k, path):
            if k < 0:
                return
            if k == 0:
                ans.append(path.copy())
                return

            for i in range(s, len(arr)):
                if i > s and arr[i] == arr[i - 1]:
                    continue
                path.append(arr[i])
                dfs(i + 1, k - arr[i], path)
                path.pop()

        arr.sort()
        dfs(0, k, [])
        return ans
