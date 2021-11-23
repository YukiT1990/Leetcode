# 952. Largest Component Size by Common Factor

# Reference
# https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/822315/Python3-official-solution-with-improvement-Largest-Component-Size-by-Common-Factor

class UF:
    def __init__(self) -> None:
        self.parent = {}
        self.sz = {}
        self.count = 0

    def add(self, p):
        if p not in self.parent:
            self.parent[p] = p
            self.sz[p] = 1
            self.count += 1

    def find(self, p: int) -> int:
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p: int, q: int) -> None:
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            self.parent[j] = i
            self.sz[i] += self.sz[j]
        else:
            self.parent[i] = j
            self.sz[j] += self.sz[i]
        self.count -= 1


# class Solution:
#     def largestComponentSize(self, nums: List[int]) -> int:
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def fac(n):
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    n //= i
                    return set((i,)) | fac(n)
            return set((n,))

        @lru_cache(None)
        def group_id(p):
            return uf.find(p)

        uf = UF()
        c = Counter()
        for n in nums:
            factors = fac(n)
            if (key := tuple(sorted(factors))) not in c:
                p = factors.pop()
                uf.add(p)
                for q in factors:
                    uf.add(q)
                    uf.union(p, q)
            c[key] += 1
        if uf.count == 1:
            return len(nums)
        groups = Counter()
        for factors, value in c.items():
            groups[group_id(factors[0])] += value
        return groups.most_common()[0][1]
