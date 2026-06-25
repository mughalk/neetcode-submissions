class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        curr_min=1001
        while l<=r:
            # check the current min if sorted
            if nums[l]<nums[r]:
                # sorted as expected
                if nums[l]<curr_min:
                    curr_min=nums[l]
                    break
            mid=(l+r)//2
            curr_min=min(curr_min,nums[mid])
            # now we check if it its a rotated/sorted split area
            # bc its rotated, u will have a sorted part, and a rotated part
            # or just a sorted part
            # what does it mean to find the sorted vs rotated part differences?
            if nums[l]<=nums[mid]:
                # so everything from 0-l is sorted up until the middle point
                # (ie rotated) then what u do is move ur search to the middle point
                # actually we have TWO SORTED PARTS, theyre just split somewhere
                l=mid+1
                # so LHS is already boring and sorted, lets find the split point
                # drop LHS and search right to find the minimum faster
            else:
                r=mid-1
                # so the smallest number on the LHS is greater than the middle
                # which means the split point is on the LHS
                # aka LHS is ROTATED and so we can find the minimum faster by checking there
        return curr_min