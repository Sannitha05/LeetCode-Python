class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def comb(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return

            if i>= len(candidates) or total>target:
                return

            candidates[i]

            curr.append(candidates[i])
            comb(i,curr,total + candidates[i])
            curr.pop()
            comb(i+1,curr,total)

        comb(0,[],0)
        return res         