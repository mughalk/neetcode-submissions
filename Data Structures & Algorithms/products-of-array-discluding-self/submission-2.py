class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product is multiplication
        output_lst=[]
        final_product=nums[0]
        zeros_array=[]
        # instead of ignoring the number, just go through each, save each, and then DIVIDE by the number
        for i in range(0, len(nums)):
            if i!=0 and nums[i]!=0:
                final_product*=nums[i]
            if nums[i]==0:
                zeros_array.append(i)
        for x in range(0, len(nums)):
            if len(zeros_array)==1:
                if nums[x]==0:
                    new_num=final_product
                else:
                    new_num=0
            elif len(zeros_array)>=2:
                new_num=0
            else:
                new_num=final_product//nums[x]
            output_lst.append(new_num)
        return output_lst
            