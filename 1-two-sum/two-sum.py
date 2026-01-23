class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {} # This is our memory: {number: index}
        i = 0
    
        while i < len(nums):
            current_num = nums[i]
            needed_num = target - current_num # The "complement"
        
         # Check if the number we need is already in our memory
            if needed_num in seen_numbers:
            # We found it! Return the index of the needed_num and the current index
               return [seen_numbers[needed_num], i]
        
            # If we haven't seen the needed_num, remember the current_num and its index
            seen_numbers[current_num] = i
        
           # Move to the next number
            i += 1
        
        return None # Return nothing if no pair is found



#ALT
def twoSum(nums, target):
    seen = {} # value : index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

print(twoSum([2, 7, 11, 15], 26)) # Output: [2, 3]
        
