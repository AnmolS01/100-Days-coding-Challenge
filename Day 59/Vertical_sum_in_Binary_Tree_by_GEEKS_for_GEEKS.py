class Solution:
    # Complete the function below
    def verticalSum(self, root):
        if not root:
            return []

        vertical_sums = {}

        def dfs(node, distance):
            if not node:
                return

            vertical_sums[distance] = vertical_sums.get(distance, 0) + node.data
            
            dfs(node.left, distance - 1)
            dfs(node.right, distance + 1)

        dfs(root, 0)

        return [vertical_sums[key] for key in sorted(vertical_sums.keys())]
