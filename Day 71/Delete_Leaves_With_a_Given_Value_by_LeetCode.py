1325. Delete Leaves With a Given Value

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if not root.left and not root.right and root.val == target:
                return None
            return root
        return dfs(root)
