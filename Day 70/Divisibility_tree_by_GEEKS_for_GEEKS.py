from typing import List


class Solution:
    def __init__(self):
        self.ans = 0
        
    def dfs(self, adj, vis, start):
        vis[start] = 1
        cnt = 0
        
        for i in adj[start]:
            if not vis[i]:
                res = self.dfs(adj, vis, i)
                if res % 2 == 0:
                    self.ans += 1
                else:
                    cnt += res
        
        return cnt + 1
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        adj = [[] for _ in range(n)]
        
        for edge in edges:
            adj[edge[0] - 1].append(edge[1] - 1)
            adj[edge[1] - 1].append(edge[0] - 1)
        
        vis = [0] * n
        self.dfs(adj, vis, 0)
        
        return self.ans


# ______________________________________________________________________________Explaination________________________________________________________________________________

# Now, let's break down the Python code step by step using the same input:

# n = 10
# edges = [[2,1],[3,1],[4,3],[5,2],[6,1],[7,2],[8,6],[9,8],[10,8]]

# Initialization:

# n = 10: Total number of nodes in the graph.
# edges: List of edges in the graph. Each edge is represented by a pair of nodes.
# Building the Adjacency List:

# We initialize an empty adjacency list adj of size n.
# We iterate through each edge in edges.
# For each edge (u, v), we add v - 1 to the adjacency list of u - 1, and vice versa. This step builds an undirected graph.
# After this step, the adjacency list adj will look like this:

# less
# Copy code
# adj[0]: [1]
# adj[1]: [0, 2, 5]
# adj[2]: [1, 3, 6]
# adj[3]: [2, 4]
# adj[4]: [3]
# adj[5]: [1]
# adj[6]: [2, 7]
# adj[7]: [6, 8, 9]
# adj[8]: [7]
# adj[9]: [7]

# Depth-First Search (DFS):

# We initialize a vis list to keep track of visited nodes, initially all set to 0.

# We call the dfs function with parameters: the adjacency list adj, the vis list, and the starting node 0.

# In the dfs function, we mark the starting node as visited (vis[start] = 1), and initialize a cnt variable to 0.

# We iterate over each adjacent node (i) of the current node start.
# If it is not visited (not vis[i]), we recursively call dfs on it.
# If the result of the recursive call res is even, we increment ans (the count of edges to be removed) by 1. Otherwise, we add res to cnt.
# We return cnt + 1, which represents the number of nodes in the subtree rooted at the current node start.
# Returning the Result:

# We return the value of ans, which represents the minimum number of edges to be removed to make each subtree of the graph have an even number of nodes.

