class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n_day = 0
        profit = 0
        first_num = prices[0]
        for i in range(len(prices)-1):
            curr = prices[i]
            next_num = prices[i+1]

            if curr < first_num:
                first_num = curr 

            check = next_num - first_num
            if check > profit:
                profit = check
    

        return profit