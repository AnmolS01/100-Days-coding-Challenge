# Problem Statement : Euler Circuit in an Undirected Graph

class Solution:
	def isEularCircuitExist(self, v, adj):
		#Code here
		for i in range(v):
            if len(adj[i]) % 2 == 1:
                return False
        
        return True

# __________________________________________________________________________________EPLAINATION_______________________________________________________________________________________

# 0 ---- 1
# |      |
# |      |
# 2 ---- 3

# Vertex 0 is adjacent to vertices 1 and 2.
# Vertex 1 is adjacent to vertices 0 and 3.
# Vertex 2 is adjacent to vertices 0 and 3.
# Vertex 3 is adjacent to vertices 1 and 2.
# Now, to determine if a vertex has an odd or even number of adjacent vertices:

# If a vertex has an odd number of adjacent vertices, it means it has an odd degree.
# If a vertex has an even number of adjacent vertices, it means it has an even degree.
# For example, in the given graph:

# Vertex 0 has an even degree because it's adjacent to 2 vertices (1 and 2), which is an even number.
# Vertex 1 has an even degree because it's adjacent to 2 vertices (0 and 3), which is an even number.
# Vertex 2 has an even degree because it's adjacent to 2 vertices (0 and 3), which is an even number.
# Vertex 3 has an even degree because it's adjacent to 2 vertices (1 and 2), which is an even number.

# Given the graph and its adjacency list, the output will be True, indicating that an Euler circuit exists in the graph because all vertices have an even degree.
