class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            found = False
            for j in range(1, n):
                next_index = (i + j) % n
                if nums[next_index] > nums[i]:
                    res.append(nums[next_index])
                    found = True
                    break
            if not found:
                res.append(-1)
        return res
