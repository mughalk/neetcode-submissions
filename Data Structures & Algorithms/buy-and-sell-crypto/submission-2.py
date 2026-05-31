class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer?
        left=0#we start with day 0
        right=1#and we compare with the immediate next day
        max_profit=0
        #len(prices) is the OUTER fixed pointer thats like the 
        # [10,1,5,6,7,1]
        # we iterate until the end of the prices list

        while right<len(prices):
            curr_profit=prices[right]-prices[left]
            if curr_profit>max_profit:
                max_profit=curr_profit
            if prices[right]<prices[left]:
                left=right
            right+=1
        return max_profit

