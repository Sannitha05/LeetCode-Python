class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        while num <= len(nums)-1:
            count = 0
            for j in nums:
                if nums[num] == j:
                    count += 1
            if count == 1:
                return nums[num]
            else:
                num += 1