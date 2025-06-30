class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def comb(i,t,path):
            if t == 0: 
                res.append(path)
                return
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > t:
                    break
                comb(j+1,t - candidates[j], path +[candidates[j]])
        comb(0,target,[])
        return res