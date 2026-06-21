class Solution:
    def isValid(self, s: str) -> bool:
        # keep track of newly opened brackets
        # keep a running list or map of newly closed brackets, should be same as opened

        brackets_expected={}
        expected_str='(){}[]'
        while '()' in s or '[]' in s or '{}' in s:
            # remember that replacing in python just creates this floating object in memory
            # and u need to tie it down to a var name!!!
            s=s.replace('()','')
            s=s.replace('[]','')
            s=s.replace('{}','')
            # this is o(n^2) complexity because we dont just pass through the string once
            # think about the worst case completely all nested brackets
            # (()) --> you do n^2 passes --> pass twice to un-nest the brackets and so that we can remove them
        return s==''
        # check if any of the frequencies are odd