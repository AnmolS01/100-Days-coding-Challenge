# 979. Distribute Coins in Binary Tree

class Solution:
    def __init__(self):
        self.count = 0
    
    def dfs(self, root):
        if not root:
            return 0
        leftCoin = self.dfs(root.left)
        rightCoin = self.dfs(root.right)

        remainingCoin = root.val + leftCoin + rightCoin -1
        self.count += abs(remainingCoin)
        return remainingCoin

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.count
