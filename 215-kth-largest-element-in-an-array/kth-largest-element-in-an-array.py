import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Build a min-heap of size k
        min_heap = nums[:k]         # Take first k elements
        heapq.heapify(min_heap)     # Turn them into a heap - O(k)

        # For every remaining element
        for num in nums[k:]:
            if num > min_heap[0]:   # If bigger than the smallest in heap
                heapq.heapreplace(min_heap, num)  # Replace the smallest

        # The root of the min-heap is the kth largest
        return min_heap[0]


# Brute force - O(n log n)
# "The simplest approach is to sort and return the kth element"
nums.sort(reverse=True)
return nums[k-1]

#Or use heap library
import heapq
# "But we can do better with a min-heap of size k - O(n log k)"
# This is faster when k is much smaller than n
return heapq.nlargest(k, nums)[-1]
