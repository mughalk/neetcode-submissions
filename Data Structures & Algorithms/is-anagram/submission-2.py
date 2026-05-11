class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_dict = {}
        t_dict = {}
        if s_len != t_len:
            return False
        return sorted(s) == sorted(t)
        # if s_len == t_len: maybe not really needed?
            # then we can continue
