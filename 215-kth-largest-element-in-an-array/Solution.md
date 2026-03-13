# Find Kth Largest Element in an Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array.

> Note: It is the kth largest element in sorted order, not the kth distinct element.

---

## Intuition

The key insight is: **we don't need to sort the entire array.**

We only need to keep track of the **k largest numbers** we have seen so far. We use a **min-heap of size k** to do this efficiently.

Think of it like a **"Top K Leaderboard"**:
- The leaderboard only holds `k` players at a time.
- The **weakest player** (smallest number) sits at the front, ready to be kicked out.
- Every time we see a new number that is **stronger** (larger) than the weakest player, we swap them out.
- At the end, the weakest player on the leaderboard (`min_heap[0]`) is the **kth largest** overall.

---

## Solution

```python
import heapq
from typing import List

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
```

---

## Complexity Analysis

### Time Complexity: O(n log k)
| Step | Operation | Cost |
|------|-----------|------|
| `heapq.heapify(min_heap)` | Build initial heap of size k | O(k) |
| Loop through remaining `n - k` elements | For each element, `heapreplace` costs O(log k) | O((n - k) log k) |
| **Total** | | **O(n log k)** |

> Why is this better than sorting?
> - Sorting the entire array = **O(n log n)**
> - This heap approach = **O(n log k)**
> - When `k` is much smaller than `n`, `log k << log n`, making this significantly faster.

### Space Complexity: O(k)
- We only store `k` elements in `min_heap` at any time.
- No matter how large `nums` is, our heap never grows beyond size `k`.

---

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|-----------------|-------|
| Brute Force (max + remove in loop) | O(k × n) | O(k) | Too slow for large inputs |
| Sorting | O(n log n) | O(1) | Simple but not optimal |
| **Min-Heap (this solution)** | **O(n log k)** | **O(k)** | **Optimal for large n, small k** |
| `heapq.nlargest` (one-liner) | O(n log k) | O(k) | Clean but hides the logic |

---

## Full Example Walkthrough

### Input
```
nums = [3, 2, 1, 5, 6, 4],  k = 2
Expected Output: 5
```

### Step 1: Build initial min-heap from first k elements
```
min_heap = nums[:2] = [3, 2]
heapq.heapify(min_heap)
min_heap = [2, 3]   ← 2 is at the top (smallest)
```

### Step 2: Loop through remaining elements nums[2:] = [1, 5, 6, 4]

#### Iteration 1: num = 1
```
Is 1 > min_heap[0] (which is 2)?
1 > 2? ❌ NO → Skip
min_heap = [2, 3]   (unchanged)
```

#### Iteration 2: num = 5
```
Is 5 > min_heap[0] (which is 2)?
5 > 2? ✅ YES → Kick out 2, add 5
heapq.heapreplace(min_heap, 5)
min_heap = [3, 5]   ← 3 is now the new smallest
```

#### Iteration 3: num = 6
```
Is 6 > min_heap[0] (which is 3)?
6 > 3? ✅ YES → Kick out 3, add 6
heapq.heapreplace(min_heap, 6)
min_heap = [5, 6]   ← 5 is now the new smallest
```

#### Iteration 4: num = 4
```
Is 4 > min_heap[0] (which is 5)?
4 > 5? ❌ NO → Skip
min_heap = [5, 6]   (unchanged)
```

### Step 3: Return min_heap[0]
```
min_heap = [5, 6]
return min_heap[0] = 5 ✅
```

### Leaderboard Trace

| Step | num | Action | min_heap | min_heap[0] |
|------|-----|--------|----------|-------------|
| Init | - | heapify [3,2] | [2, 3] | 2 |
| 1 | 1 | Skip (1 < 2) | [2, 3] | 2 |
| 2 | 5 | Replace 2 with 5 | [3, 5] | 3 |
| 3 | 6 | Replace 3 with 6 | [5, 6] | 5 |
| 4 | 4 | Skip (4 < 5) | [5, 6] | 5 |
| **Answer** | | | | **5** ✅ |

---

## Key Concepts

### What is a Min-Heap?
A min-heap is a binary tree where the **smallest value is always at the root (top)**. In Python, `heapq` implements a min-heap using a regular list.

```
      2
     / \
    3   5
```
- `heap[0]` is always the smallest element.
- Adding/removing costs **O(log n)**.

### Why min-heap and not max-heap?
- A **max-heap** would put the largest at the top — but we already know the largest, we want the **kth largest**.
- A **min-heap of size k** keeps the k largest numbers, with the **smallest of those k** at the top — which is exactly the kth largest!

---

## Edge Cases

```python
# Edge case 1: k = 1 (find the largest)
nums = [3, 2, 1], k = 1
Output: 3

# Edge case 2: k = len(nums) (find the smallest)
nums = [3, 2, 1], k = 3
Output: 1

# Edge case 3: Negative numbers
nums = [-1, -2, -3, -4], k = 2
Output: -2

# Edge case 4: Duplicates
nums = [3, 3, 3, 3], k = 2
Output: 3
```

---

## LeetCode Info
- **Problem**: 215. Kth Largest Element in an Array
- **Difficulty**: Medium
- **Tags**: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
