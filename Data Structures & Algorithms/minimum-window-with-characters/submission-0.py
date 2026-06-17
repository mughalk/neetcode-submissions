class Solution:
    def minWindow(self, s: str, t: str) -> str:
            # have = how many unique chars currently we have that satisfy required frequency
            # need = how many unique chars we need to satisfy
            
            # could we not make this into a dictionary?
            # once you HAVE what you need, end and return
            if len(t)>len(s):
                return ""
                # invalid
            l = 0
            t_freq={}
            res=[-1,-1]
            resLen=float("infinity")
            window_map={}
            for k in range(len(t)):
                t_freq[t[k]]=1+t_freq.get(t[k],0)

            have, need = 0, len(t_freq)
            for r in range(len(s)):
                window_map[s[r]]=1+window_map.get(s[r],0)
                # current running total frequency map for our window
                # while frequency of all values in window is not same as values in t_freq
                if s[r] in t_freq and window_map[s[r]]==t_freq[s[r]]:
                    have+=1
                    # we compare the frequencies so that we actually CAN have a unique "have" value
                    # but the have value is correct, it encompasses our fulfilment of the correct frequency of a unique character
                    # so we're not just seeing the character, we're seeing what it represents in numbers as well
                while have==need:
                    # we want to MINIMIZE cus we want shortest
                    # res=[l,r]
                    if r-l+1<resLen:
                        res=[l,r]
                        resLen=r-l+1
                    window_map[s[l]]-=1
                    # now lets see the consequences of shrinking 1 from the left
                    if s[l] in t_freq and window_map[s[l]]<t_freq[s[l]]:
                        # uh oh, we had the correct frequency but now we don't!
                        have-=1
                    l+=1
            # we add a +1 because string indices in python are INCLUSIVE on the first index
            # but EXCLUSIVE on the second one
            return s[res[0]:res[1]+1]


