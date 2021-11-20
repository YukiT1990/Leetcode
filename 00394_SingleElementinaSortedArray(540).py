# 540. Single Element in a Sorted Array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # nums_odd = [nums[x] for x in range(0, len(nums), 2)]
        # nums_even = [nums[x] for x in range(1, len(nums), 2)]
        # # print(nums_odd)
        # # print(nums_even)
        # for num in nums_odd:
        #     if num not in nums_even:
        #         return num

        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == nums[mid-1]:  # duplicate found
                if mid % 2:       # target > mid
                    lo = mid+1  # exclude second index mid; mid+1
                else:           # target < mid
                    hi = mid-2  # exclude first index mid-1; mid-1-1
            elif nums[mid] == nums[mid+1]:  # duplicate found
                if mid % 2:       # target < mid
                    hi = mid-1  # exclude first index mid; mid-1
                else:           # target > mid
                    lo = mid+2  # exclude second index mid+1; mid+1+1
            else:  # no duplicate found, target == mid
                return nums[mid]
        return nums[lo]

        # lo, hi = 0, len(nums)-2  # hi starts from an even index so that hi^1 gives the next odd number
        # while lo <= hi:
        #     mid = lo+(hi-lo)//2
        #     if nums[mid] == nums[mid^1]:
        #         lo = mid+1
        #     else:
        #         hi = mid-1
        # return nums[lo]
