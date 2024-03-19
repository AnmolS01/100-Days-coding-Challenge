#problem Statement: Possible Paths in a Tree

class Solution:
    def __init__(self):
        self.ans = 0

    def root(self, i, parent):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(self, a, b, parent, sz):
        ra = self.root(a, parent)
        rb = self.root(b, parent)
        if ra == rb:
            return sz[ra] * sz[ra]
        if sz[ra] < sz[rb]:
            ra, rb = rb, ra
            a, b = b, a
        self.ans += sz[ra] * sz[rb]
        parent[rb] = ra
        sz[ra] += sz[rb]
        return self.ans

    def maximumWeight(self, n, edges, q, queries):
        self.ans = 0
        parent = [i for i in range(n + 1)]
        sz = [1] * (n + 1)
        wt = [(edges[i][2], (edges[i][0], edges[i][1])) for i in range(n - 1)]
        wt.sort()
        mp = {}
        for i in range(n - 1):
            a, (b, c) = wt[i]
            mp[a] = self.union(b, c, parent, sz)
        res = []
        for i in range(q):
            val = next((v for v in reversed(sorted(mp.keys())) if v <= queries[i]), None)
            if val is None:
                res.append(0)
            else:
                res.append(mp[val])
        return res
