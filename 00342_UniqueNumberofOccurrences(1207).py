# 1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr = dict()
        for d in arr:
            if d not in dict_arr.keys():
                dict_arr[d] = 1
            else:
                dict_arr[d] += 1
        arr_list = sorted(list(dict_arr.values()))
        # print(arr_list)
        for i in range(len(arr_list) - 1):
            if arr_list[i] == arr_list[i+1]:
                return False
        return True
        