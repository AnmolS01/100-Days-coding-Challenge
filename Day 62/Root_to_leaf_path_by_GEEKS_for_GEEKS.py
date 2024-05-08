class Solution:
    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        paths = []
        if not root:
            return paths
        
        def dfs(node, current_path):
            if not node:
                return
            current_path.append(node.data)
            
            if not node.left and not node.right:
                # If it's a leaf node, add the current path to paths
                paths.append(list(current_path))  # Make a copy of the current_path
            else:
                dfs(node.left, current_path)
                dfs(node.right, current_path)
            current_path.pop()  # Backtrack
            
        dfs(root, [])
        return paths
