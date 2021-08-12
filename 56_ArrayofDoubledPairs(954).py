# 954. Array of Doubled Pairs

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # key: each element in arr, value: the number of occurrence
        c = Counter(arr)
        print(c)
        for n in sorted(c.keys(), key=abs): # to sort a sequence of numbers based on their absolute value
            # There is new syntax := that assigns values to variables as part of a larger expression.
            # Reference(https://docs.python.org/3/whatsnew/3.8.html)
            while c[n] > 0 and c[(double := 2 * n)] > 0:
                # If there are n and 2n in the keys, remove them.
                c[n] -= 1
                c[double] -= 1
                print([v for v in c.values()])
        return all(not v for v in c.values())
        # If all of the number of each element in arr is 0, return true, otherwise return false.
        # The all() function returns True if all elements in the given iterable are true. If not, it returns False.
