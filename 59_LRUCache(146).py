# 146. LRU Cache

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        # make the least recently used key last in the dict
        val = self.dict.pop(key)
        self.dict[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]  # delete the oldest
        self.dict[key] = value  # dd the key-value pair to the cache

    #  del keyword can be used to inplace delete the key that is present in the dictionary. One drawback that can be thought of using this is that is raises an exception if the key is not found and hence non-existence of key has to be handled.
    #  The next() function returns the next item from the iterator.
    #  The Python iter() function returns an iterator for the given object.
    # list of vowels
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     vowels_iter = iter(vowels)

#     print(next(vowels_iter))    # 'a'
#     print(next(vowels_iter))    # 'e'
#     print(next(vowels_iter))    # 'i'
#     print(next(vowels_iter))    # 'o'
#     print(next(vowels_iter))    # 'u'


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Reference
# https://leetcode.com/problems/lru-cache/discuss/850110/Python-3.7%2B.-No-need-to-use-OrderedDict.-Simply-use-the-regular-dict
