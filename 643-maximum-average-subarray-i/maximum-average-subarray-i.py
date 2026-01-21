class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum=0
        for i in range(k):
            win_sum+=nums[i]
       
        
        max_sum = win_sum

        for i in range (k, len(nums)):
            win_sum-=nums[i-k]
            win_sum+=nums[i]
        
            if win_sum > max_sum:
                max_sum = win_sum
        return max_sum / k
        
