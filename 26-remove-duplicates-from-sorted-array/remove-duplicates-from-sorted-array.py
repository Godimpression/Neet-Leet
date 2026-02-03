class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'k' keeps track of where to place the next unique element
        k = 1 
        
        for i in range(1, len(nums)):
            # If current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Move it to the 'k' position
                nums[k] = nums[i]
                k += 1
        
        # Return the count of unique elements
        return k