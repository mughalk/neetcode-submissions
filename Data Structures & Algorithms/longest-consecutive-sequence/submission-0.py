class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # each element exactly ONE greater than index-1
        # can you not just sort the array and figure that out?
        #default sort is ascending, which is what we want
        if len(nums)==0:
            return 0
        nums_sorted_cpy=sorted(nums)
        old_longest_counter=1
        new_longest_counter=1
        curr_longest_counter=1
        curr_longest_sequence={}
        # 1, 1, 3 = 1
        # 1, 3
        # how do u deal with duplicates
        # 1,1,1,2 = 2
        # 1,3,5,6,7
        # 1,2,3,5,6
        # 1,2,3,5,6,8,9,10,11
        removed_duplicates=list(dict.fromkeys(nums_sorted_cpy))
        for i in range(0, len(removed_duplicates)):
            if i<len(removed_duplicates)-1:
                diff = removed_duplicates[i+1]-removed_duplicates[i]
                if diff==1:
                    curr_longest_counter+=1
                else:
                    # streak is complete, save the sequence count, and start up a new count
                    # only save the new longest count as the true_longest_count if its greater than old_longest_count
                    # is the current count greater than the immediate past?, if yes, then put it as the old
                    # else, dont save it
                    if curr_longest_counter>old_longest_counter:
                        old_longest_counter=curr_longest_counter
                        # lose the past and switch it for the curr longest count
                    # start a new streak
                    new_longest_counter=1
                    curr_longest_counter=new_longest_counter
                    # something about sorting is afoot here; it only compares immediate past and present
                    # what about all the sequences in between?

        return max(old_longest_counter, curr_longest_counter)
            # check if next element is smaller than current element or not
            # if nums[i]>nums[i-1] or nums[i+1]>nums[i] then counter+=1
        # find a set?
        # curr_longest_set=set(nums_sorted_cpy)
        # 1, 2
        # prev_elem=0
        # curr_elem=0
        # return len(curr_longest_set)
        # for idx, i in enumerate(curr_longest_set):
        #     if idx!=0:
        #         if 
