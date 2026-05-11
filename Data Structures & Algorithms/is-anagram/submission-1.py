class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_dict = {}
        t_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        for char2 in t:
            if char2 not in t_dict:
                t_dict[char2] = 1
            else:
                t_dict[char2] += 1
        if s_dict.items() == t_dict.items():
            return True
        return False
        # if s_len == t_len: maybe not really needed?
            # then we can continue
