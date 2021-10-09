# 1426. Counting Elements

class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr = sorted(arr)
        arr_dict = dict()
        for k in arr:
            if k not in arr_dict.keys():
                arr_dict[k] = 1
            else:
                arr_dict[k] += 1
        key_list = list(arr_dict.keys())
        
        result = 0
        for i in range(len(key_list)-1):
            if key_list[i+1] == key_list[i] + 1:
                result += arr_dict[key_list[i]]
        return result