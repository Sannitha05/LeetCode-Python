class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def subsets(index,curr):
            ans.append(curr[:])
            for i in range(index,len(nums)):
                if i > index and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                subsets(i+1,curr)
                curr.pop()
        subsets(0,[])
        return ans