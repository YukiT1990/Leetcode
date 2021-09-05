# 703. Kth Largest Element in a Stream

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # 7936 ms	18.6 MB
        # self.nums = sorted(nums)
        # self.k = k
        
        # 88 ms	18.1 MB	
        # Reference
        # https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/456280/Python3-min-heap-for-k-largest-element
        self.heap = []
        self.k = k
        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            else:
                if i > self.heap[0]:
                    heapq.heappushpop(self.heap, i)

    def add(self, val: int) -> int:
        # self.nums.sort()
        # index = bisect.bisect_right(self.nums, val)
        # self.nums.insert(index, val)
        # self.nums.sort(reverse=True)
        # return self.nums[self.k-1]
    
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)      
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)