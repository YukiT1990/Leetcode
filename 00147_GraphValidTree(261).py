# 261. Graph Valid Tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and len(edges) == 0:
            return True
        if len(edges) >= n:
            return False
        node_dict = {}
        for edge in edges:
            if edge[0] not in node_dict.keys():
                node_dict[edge[0]] = [edge[1]]
            else:
                node_dict[edge[0]].append(edge[1])
            if edge[1] not in node_dict.keys():
                node_dict[edge[1]] = [edge[0]]
            else:
                node_dict[edge[1]].append(edge[0])
                
        
        for value in node_dict.values():
            if len(value) < 1:
                return False
        
        def detect_cycle(node, visited, parent):
            visited.add(node)
            for child in node_dict[node]:
                if(child == parent): 
                    continue
                if(child in visited or detect_cycle(child, visited, node)):
                    return True       
            return False 
        # print(node_dict)
        seen = set()
        if 0 not in node_dict.keys():
            return False
        if detect_cycle(0, seen, -1):
            return False
        return len(seen) == n
            
            
        