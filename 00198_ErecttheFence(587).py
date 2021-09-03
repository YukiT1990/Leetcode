# 587. Erect the Fence

# Reference
# https://leetcode.com/problems/erect-the-fence/discuss/705406/Python-Simple-to-understand-Convex-Hull
class Solution:
    # def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
#         min_x = 100
#         min_y = 100
#         max_x = 0
#         max_y = 0
        
#         for x, y in trees:
#             min_x = min(min_x, x)
#             min_y = min(min_y, y)
#             max_x = max(max_x, x)
#             max_y = max(max_y, y)
            
#         result = []
#         # left_y: smallest y among that having min_x, bottom_x: smallest x among that having min_y
#         left_bottom = {"left": [min_x, 100], "bottom": [100, min_y]}
#         left_upper = {"left": [min_x, 0], "upper": [100, max_y]}
#         right_bottom = {"right": [max_x, 100], "bottom": [0, min_y]}
#         right_upper = {"right": [max_x, 0], "upper": [0, max_y]}
#         for tree in trees:
#             if tree[0] == min_x or tree[0] == max_x or tree[1] == min_y or tree[1] == max_y:
#                 result.append(tree)
#                 if tree[0] == min_x:
#                     left_bottom["left"][1] = min(left_bottom["left"][1], tree[1])
#                     left_upper["left"][1] = max(left_upper["left"][1], tree[1])
#                 if tree[0] == max_x:
#                     right_bottom["right"][1] = min(right_bottom["right"][1], tree[1])
#                     right_upper["right"][1] = max(right_upper["right"][1], tree[1])
#                 if tree[1] == min_y:
#                     left_bottom["bottom"][0] = min(left_bottom["bottom"][0], tree[0])
#                     right_bottom["bottom"][0] = max(right_bottom["bottom"][0], tree[0])
#                 if tree[1] == max_y:
#                     left_upper["upper"][0] = min(left_upper["upper"][0], tree[0])
#                     right_upper["upper"][0] = max(right_upper["upper"][0], tree[0])
        
#         if left_bottom["bottom"][1] != left_bottom["left"][1] and left_bottom["bottom"][0] != left_bottom["left"][0]:
#             left_bottom["a"] = (left_bottom["bottom"][1] - left_bottom["left"][1]) / (left_bottom["bottom"][0] - left_bottom["left"][0])
#             left_bottom["b"] = left_bottom["bottom"][1] - left_bottom["a"] * left_bottom["bottom"][0]
#             for tree in trees:
#                 if tree[1] <= tree[0] * left_bottom["a"] + left_bottom["b"] and tree not in result:
#                     result.append(tree)
                    
#         if left_upper["upper"][1] != left_upper["left"][1] and left_upper["upper"][0] != left_upper["left"][0]:
#             left_upper["a"] = (left_upper["upper"][1] - left_upper["left"][1]) / (left_upper["upper"][0] - left_upper["left"][0])
#             left_upper["b"] = left_upper["upper"][1] - left_upper["a"] * left_upper["upper"][0]
#             for tree in trees:
#                 if tree[1] >= tree[0] * left_upper["a"] + left_upper["b"] and tree not in result:
#                     result.append(tree)
                    
#         if right_bottom["bottom"][1] != right_bottom["right"][1] and right_bottom["bottom"][0] != right_bottom["right"][0]:
#             right_bottom["a"] = (right_bottom["bottom"][1] - right_bottom["right"][1]) / (right_bottom["bottom"][0] - right_bottom["right"][0])
#             right_bottom["b"] = right_bottom["bottom"][1] - right_bottom["a"] * right_bottom["bottom"][0]
#             for tree in trees:
#                 if tree[1] <= tree[0] * right_bottom["a"] + right_bottom["b"] and tree not in result:
#                     result.append(tree)
                    
#         if right_upper["upper"][1] != right_upper["right"][1] and right_upper["upper"][0] != right_upper["right"][0]:
#             right_upper["a"] = (right_upper["upper"][1] - right_upper["right"][1]) / (right_upper["upper"][0] - right_upper["right"][0])
#             right_upper["b"] = right_upper["upper"][1] - right_upper["a"] * right_upper["upper"][0]
#             for tree in trees:
#                 if tree[1] >= tree[0] * right_upper["a"] + right_upper["b"] and tree not in result:
#                     result.append(tree)
                
#         print(left_bottom)
#         print(left_upper)
#         print(right_bottom)
#         print(right_upper)
#         # print(result)
#         return result
    
    @staticmethod
    def check_cross_product(a, b, o):
        ax = a[0] - o[0]
        ay = a[1] - o[1]
        bx = b[0] - o[0]
        by = b[1] - o[1]
        return ax*by - ay*bx

    @staticmethod
    def find_farthest_pt(pts, pt):
        far = None
        for val in pts:
            if not far:
                far = tuple(val)
            else:
                dist_new = (val[0] - pt[0]) ** 2 + (val[1] - pt[1]) ** 2
                dist_old = (far[0] - pt[0]) ** 2 + (far[1] - pt[1]) ** 2
                if dist_new > dist_old:
                    far = tuple(val)
        return far

    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:

        ltm_pt = None
        for val in points:
            if not ltm_pt:
                ltm_pt = tuple(val)
            elif val[0] < ltm_pt[0]:
                ltm_pt = tuple(val)

        tree_dict = set()
        vis = {}
        curr_pt = ltm_pt
        while(curr_pt and curr_pt not in vis):
            tree_dict.add(curr_pt)
            found_pt = []
            for val in points:
                if tuple(val) != curr_pt:
                    if not found_pt:
                        found_pt.append(val)
                    else:
                        crp_prd = Solution.check_cross_product(found_pt[0], val, curr_pt)
                        if crp_prd > 0:
                            found_pt = []
                            found_pt.append(val)
                        elif not crp_prd:
                            found_pt.append(val)
            vis[curr_pt] = True
            farthest_pt = Solution.find_farthest_pt(found_pt, curr_pt)
            for val in found_pt:
                tup = tuple(val)
                tree_dict.add(tup)
            curr_pt = farthest_pt
        return tree_dict
        
        