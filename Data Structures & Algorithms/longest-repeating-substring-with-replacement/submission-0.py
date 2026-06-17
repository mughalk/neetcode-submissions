class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # basically, we still want the longest substring, but this time,
        # with duplicates
        # we are allowed maximum k letters to replace to any other character we like
        # these chars can be dynamic ofc, chosen from the string s itself
        no_repeated_chars=set()
        left=0
        char_freq={}
        l=0
        longest_substring=0
        # right=len(s)-1
        #maybe also keep track of replacements needed for when the value appears next in the string?

        for r in range(len(s)):
            # iterate through the substring too though so that we can match the letter frequency to the hashmap?
            
            # here what we r doing is either iterating the frequency or setting the frequency of what we DO have
            # char_freq[s[r]]=1+char_freq.get(s[r],0)
            if s[r] in char_freq:
                char_freq[s[r]]+=1
            else:
                char_freq[s[r]]=1
            # we r constructing char_freq as we go so technically its the most
            # frequent character that we've seen so far, which is why we're
            # allowed to do max because this max isnt a FUTURE max
            # its a max that we've already counted within our sliding window
            while (r-l+1)-max(char_freq.values())>k:
                # while the length of our window minus the highest frequency of a character within it is not able to be replacable
                # no_repeated_chars.remove(s[l])
                char_freq[s[l]]-=1
                l+=1
                # shrink from the left and remove the frequency since we're moving our sliding window
                # why do we do this?, because we're effectively sliding the window
                # shrinking it from the left, so the character frequency dict
                # actually DOES accurately represent the current sliding window
                # aka its not just the ENTIRE strings char frequencies,
                # but specifically the one for the sliding window
                # and keep in mind that our mathematics here is that
                # current window length (ie 4) - number of times most frequent character appears in the window
                # this equals how many REPLACEMENTS we'll have to do
                # and we keep shrinking the left until we have either k or less replacements that we can do;
                # hence, in that case, it IS a VALID string
                
                # this is a DYNAMIC size sliding window
            # in this method, if it IS valid, then keep stretching it to the RIGHT
            # thats why we dont define the inner loop by maintaining the valid condition
            # but rather by CONTINUING TO NOT BE the valid condition we SHRINK from the left
            # and EXPAND when it IS valid
            longest_substring=max(longest_substring,r-l+1)
        return longest_substring