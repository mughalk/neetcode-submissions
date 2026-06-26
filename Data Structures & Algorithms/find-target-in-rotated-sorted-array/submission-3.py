class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        # pivot=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
                # pivot=l
            else:
                r=mid-1
        # pivot should always be defined, by default its the left number anyway
        # cus fully rotated, the "pivot" would be l=0th index
        pivot=l

        # we add an additional layer of fine tuning by adding the b_search method
        # alternatively, replicate the below code twice
        # either way, do a standard binary search on LHS first (0-> pivot)
        # then on RHS (pivot -> len of array) and see what we get
        def b_search(l: int, r: int) -> int:
            while l<=r:
                if nums[l]==target:
                    return l
                if nums[r]==target:
                    return r
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif target>=nums[mid]:
                    l=mid+1
                    # could we somehow do a check by closeness?
                else:
                    r=mid-1
            return -1
        res=b_search(0, pivot-1)
        if res==-1:
            res=b_search(pivot,len(nums)-1)
        return res