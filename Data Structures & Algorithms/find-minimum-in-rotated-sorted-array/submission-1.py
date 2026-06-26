class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        curr_min=1001
        while l<=r:
            if nums[l]<nums[r]:
                # already sorted, just return the nums[l]
                if nums[l]<curr_min:
                    # curr_min=nums[l]
                    return nums[l]
            mid=(l+r)//2
            curr_min=min(curr_min, nums[mid])
            if nums[mid]>=nums[l]:
                # leftside is already sorted
                # so there must be a different sorted area within the array
                # that we can search, so change our mission to finding that
                l=mid+1
                # also since its greater than, its clearly not gonna be the min
                # so exclusively check the RHS 
            else:
                r=mid-1
        return curr_min
