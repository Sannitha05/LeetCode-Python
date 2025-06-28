class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(index,curr):
            if index == len(nums):
                ans.append(curr[:])
                return
            sub(index+1,curr)
            curr.append(nums[index])
            sub(index+1,curr)
            curr.pop()
        ans = []
        sub(0, [])
        return ans
        