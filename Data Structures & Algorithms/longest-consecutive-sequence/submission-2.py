class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # dont have to be consecutive in original array, so can sort
        # this is already ascending by default
        nums_sorted = sorted(nums)
        nums_no_dupes = list(set(sorted(nums)))
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        curr_sequence_length=1
        longest_sequence_length=1

        # for num in nums_no_dupes:
        #     if (num+1) in nums_no_dupes:
        #         curr_sequence_length=1
        #         while (num+curr_sequence_length) in nums_no_dupes:
        #             curr_sequence_length+=1
        #         longest_sequence_length=max(curr_sequence_length,longest_sequence_length)
        # return longest_sequence_length
        # or will this alr be considered if we do exactly +1?
        for i in nums_no_dupes:
            # is next value either the end of the list or is it 1 bigger?
            if i+1 in nums_no_dupes:
                curr_sequence_length=1
                iterator=1
                while (i+iterator) in nums_no_dupes:
                    iterator+=1
                    # this is literally just iteration by 1; check if 1+1=2 in set
                    # say i=7, then check if i+(iterator, say j=1) in set
                curr_sequence_length=iterator
                if curr_sequence_length>longest_sequence_length:
                    longest_sequence_length=curr_sequence_length
                    # curr_sequence_length=1
                    # doing the same code twice
        return max(curr_sequence_length, longest_sequence_length)
