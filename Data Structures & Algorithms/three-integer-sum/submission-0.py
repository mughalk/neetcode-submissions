class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # might need a 3 pointer?
        # no duplicates
        # list of lists
        # always remember 2pointer, 3pointer, etc, array must FIRST be sorted
        snums=sorted(nums)
        # and remove duplicates ig?
        # incorrect below, we're supposed to remove DUPLICATE index triplets
        # snums2=list(dict.fromkeys(snums))
        # -4,-1,-1,0,1,2
        #unsure about the middle calculations ie
        # 1,2,3,4
        # 3 numbers that add up to 0 where left!=middle!=right
        three_sum=[]
        # would it be a 3 pointer?; not really, maybe just keep an outer loop?
        # fixed number

        #last problem for today i think
        # would it be left<right instead?
        for i in range(0, len(snums)):
            left=i+1
            right=len(snums)-1
            fixed_num=snums[i]
            if fixed_num>0:
                # no point continuing since its all sorted
                # nothing after this number will net us a zero sum
                break
            if i > 0 and fixed_num==snums[i-1]:
                #why??; this means our fixed number is the same as the last number, so we skip this loop iteration
                # because its a DUPLICATE
                continue
            while left<right:
                # make sure u use the SORTED array not the default one
                # else our comparisons wont make sense in terms of balancing the seesaw
                curr_sum=fixed_num+snums[left]+snums[right]
                if curr_sum==0:
                    three_sum.append([snums[i],snums[left],snums[right]])
                    left+=1
                    right-=1
                    while snums[left]==snums[left-1] and left<right:
                        left+=1
                if curr_sum<0:
                    # shift left "up" 1 and/or shift left up 1; iterate
                    left+=1
                elif curr_sum>0:
                    right-=1
            # when do we iterate on the left?
        return three_sum

