class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=s.lower()
        s2 = ''.join(filter(str.isalnum, t))
        left=0
        right=len(s2)-1
        while left<right:
            # make sure the character is alphanumeric
            # or really, what does it mean to IGNORE all non-alphanumeric characters?
            if s2[left]!=s2[right]:
                return False
            left+=1
            right-=1
        return True