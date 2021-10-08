# 208. Implement Trie (Prefix Tree)

class Trie:

    def __init__(self):
        self.arr = []

    def insert(self, word: str) -> None:
        self.arr.append(word)

    def search(self, word: str) -> bool:
        return word in self.arr

    def startsWith(self, prefix: str) -> bool:
        if len(self.arr) == 0:
            return False
        N = len(prefix)
        for w in self.arr:
            if N <= len(w) and w[:N] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)