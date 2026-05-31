class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # keep track of height AND width
        # height is only considered for the minimum height between 2 pairs
        # we want surface area, so do minimum(height) * width
        # essentially we want to optimize; whatever the largest product is, we want
        # find largest product in a list
        # use 2 pointers?
        # TWO POINTER NEEDS TO BE SORTED; actually nvm i guess not for this example
        # sort_heights=sorted(heights)
        left=0
        right=len(heights)-1
        # curr_container_size=0
        largest_container_size=0


        while left<right:
            product=min(heights[left], heights[right])*(right-left)
            # if its a two pointer we need to find some criteria to move left or right with
            if product>largest_container_size:
                largest_container_size=product
                # left+=1
                # right-=1
                # continue
            if heights[left]<=heights[right]:
                # move the pointer, find a different bar so we can store more water height wise
                left+=1
            elif heights[right]<heights[left]:
                right-=1
        return largest_container_size