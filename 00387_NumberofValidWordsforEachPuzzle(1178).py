# 1178. Number of Valid Words for Each Puzzle

# Reference
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/1567415/Python-TrieBitmasking-Solutions-with-Explanation

# class TrieNode:
#     def __init__(self, ch: Optional[str] = ''):
#         self.ch = ch
#         self.count = 0
#         self.children = {}

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def add(self, word: str) -> None:
#         node = self.root
#         for ch in word:
#             if ch not in node.children.keys():
#                 node.children[ch] = TrieNode(ch)
#             node = node.children[ch]
#         node.count += 1
    
#     def search(self, word: str) -> int:       
#         def dfs(node: TrieNode, found: Optional[bool] = False) -> int:
#             result = node.count*found
#             for ch in word:
#                 if ch in node.children.keys():
#                     result += dfs(node.children[ch], found or ch == word[0])
#             return result
#         return dfs(self.root)



class Solution:
    # def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
    #     trie = Trie()
    #     for word in words:
    #         trie.add(word)
    #     return [trie.search(word) for word in puzzles]
    
    def mask(self, word: str) -> int:
        result = 0
        for ch in word:
            result |= 1 << (ord(ch)-ord('a'))
        return result

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_count = Counter(self.mask(word) for word in words)
        result = []
        for puzzle in puzzles:
            original_mask, first = self.mask(puzzle[1:]), self.mask(puzzle[0])
            curr_mask, count = original_mask, word_count[first]
            while curr_mask:
                count += word_count[curr_mask|first]
                curr_mask = (curr_mask-1)&original_mask
            result.append(count)
        return result