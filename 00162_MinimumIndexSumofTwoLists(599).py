# 599. Minimum Index Sum of Two Lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
          # 416 ms	14.9 MB
        common = [r for r in list1 if r in list2]
        index_dict = {}
        min_index_sum = 2000
        for res in common:
            index_sum = list1.index(res) + list2.index(res)
            min_index_sum = min(min_index_sum, list1.index(res) + list2.index(res))
            if index_sum in index_dict.keys():
                index_dict[index_sum].append(res)
            else:
                index_dict[index_sum] = [res]
                
        return index_dict[min_index_sum]
    

        # 185 ms	14.9 MB
        # Reference 
        # https://leetcode.com/problems/minimum-index-sum-of-two-lists/discuss/932010/Python-dict.-Time%3A-O(N%2BM).-Space%3A-O(N)
        # words1 = {word: idx for idx, word in enumerate(list1)}
        # # print(words1)
        # # {'Shogun': 0, 'Tapioca Express': 1, 'Burger King': 2, 'KFC': 3}


        # min_sum = math.inf
        # for idx2, word2 in enumerate(list2):
        #     if word2 in words1:
        #         if words1[word2] + idx2 < min_sum:
        #             min_sum = words1[word2] + idx2
        #             min_words = [word2]
        #         elif words1[word2] + idx2 == min_sum:
        #             min_words.append(word2)
                   
        # return min_words