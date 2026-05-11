class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_count_dict = {}
        t_count_dict = {}
        if s==t:
            return True
        if s_len==t_len:
            # then continue to check for letters:
            for c in s:
                if c not in t:
                    return False
                if c not in s_count_dict:
                    s_count_dict[c]=1
                elif c in s_count_dict:
                    s_count_dict[c]+=1
            for d in t:
                # both are the same below, no?
                if d not in t:
                    return False
                if d not in t_count_dict:
                    t_count_dict[d]=1
                elif d in t_count_dict:
                    t_count_dict[d]+=1
            return t_count_dict==s_count_dict
        else:
            return False
        