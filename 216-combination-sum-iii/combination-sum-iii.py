class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def combsum(index,sum,curr):
            if len(curr)==k and sum==n:
                ans.append(curr[:])
                return
            if len(curr)>k or sum>n:
                return
            for i in range(index,10):
                curr.append(i)
                combsum(i+1,sum+i,curr)
                curr.pop()
        combsum(1,0,[])
        return ans