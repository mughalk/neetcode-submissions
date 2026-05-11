class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_summed = []
        nums_len = len(nums)
        two_sum_found = False
        for i in range(nums_len):
            for j in range(i+1,nums_len):
                if nums[i] + nums[j] == target:
                    two_summed.append(i)
                    two_summed.append(j)
                    return two_summed