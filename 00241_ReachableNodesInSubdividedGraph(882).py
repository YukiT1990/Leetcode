# 882. Reachable Nodes In Subdivided Graph

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        def bfs():
            q = [(maxMoves, 0, -1)] 
            v = {0: maxMoves}       
            while q:
                next_level = []
                for m, n, p in q:
                    v[n] = max(v.get(n, -math.inf), m)
                    for neigh in g[n]:
                        c = cost[(n, neigh)]
                        if (neigh != p) and (c <= m) and (v.get(neigh, -math.inf) < (m - c)):
                            next_level.append((m-c, neigh, n))
                q = next_level
            return v

        # 1. Convert list of edges to a graph
        cost = collections.defaultdict(int)        
        g = collections.defaultdict(list)
        for a, b, n in edges:
            g[a].append(b)
            g[b].append(a)
            cost[(a,b)] = cost[(b,a)] = n + 1

        # 2. Make a map v where v[node] = number of steps remaining after reaching node
        v = bfs()

        # 3. From each pair of original nodes try to visit all of the new nodes that connect them.
        new_nodes = sum(min(v.get(a, 0) + v.get(b, 0), n) for a, b, n in edges)
        original_nodes = len(v)

        return original_nodes + new_nodes