class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        no_repeated_chars=set()
        left=0
        right=len(s)-1
        if len(s)>=2:
            right=1
        else:
            return len(s)
        longest_substring=0
        l=0
        # while left<right:
        #     no_repeated_chars.add(s[left])
            
        #     # ie zxyzxyz
        #     # xxxx
        #     if s[right] not in no_repeated_chars:
        #         no_repeated_chars.add(s[right])
        #         right+=1
        #     else:
        #         while s[left] in no_repeated_chars:
        #             left+=1
        for r in range(len(s)):
            while s[r] in no_repeated_chars:
                no_repeated_chars.remove(s[l])
                l+=1
                # this is a fixed size sliding window, u just keep moving to the right by 1
                # and ofc u keep track of the longest substring size by the SIZE of the set
                # bc the set is not including duplicates, but it is also IN ORDER 
                # so thats why we use sets as our object of choice
            no_repeated_chars.add(s[r])
            longest_substring=max(longest_substring,len(no_repeated_chars))
        return longest_substring

         