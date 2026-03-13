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
