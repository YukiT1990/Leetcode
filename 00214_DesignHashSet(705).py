# 705. Design HashSet

# using list
# 1547 ms	18.6 MB

# using hash table
# 169 ms	19.2 MB
# Reference
# https://leetcode.com/problems/design-hashset/discuss/768951/Python-simple-solution-(no-cheating)-with-complete-explanation-(video-%2B-code)

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.hashset = list()
        self.size = 10000
        self.table = [None] * self.size
        
    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        # if key not in self.hashset:
        #     self.hashset.append(key)
        hv = self.calculate_hash_value(key)
        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)
        

    def remove(self, key: int) -> None:
        # if key in self.hashset:
        #     self.hashset.remove(key)
        hv = self.calculate_hash_value(key)
        if self.table[hv] != None:
            while key in self.table[hv]:
                self.table[hv].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        # if key in self.hashset:
        #     return True
        # else:
        #     return False
        hv = self.calculate_hash_value(key)
        if self.table[hv] != None:
            return key in self.table[hv]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)