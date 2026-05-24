class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reverse the string
        new_build=''
        for c in s:
            if c.isalnum():
                new_build+=c.lower()
        return new_build==new_build[::-1]