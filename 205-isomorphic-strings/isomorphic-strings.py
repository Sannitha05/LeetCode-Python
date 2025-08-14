class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        map_t_s = {}
        for ch_s, ch_t in zip(s, t):
            if map_s_t.get(ch_s, ch_t) != ch_t or map_t_s.get(ch_t, ch_s) != ch_s:
                return False
            map_s_t[ch_s] = ch_t
            map_t_s[ch_t] = ch_s
        return True
