class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = {}
        for num in nums:
            if num not in num_frequency:
                num_frequency[num]=1
            else:
                num_frequency[num]+=1
        #bc we want to sort based on the values, but we want to store the keys
        arr = sorted(num_frequency.items(), key=lambda x:x[1])
        res=[]
        for i in range(0,k):
            # bc they are tuples
            res.append(arr.pop()[0])
        return res