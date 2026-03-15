# 198. House Robber

**Difficulty:** Medium | **Topic:** Dynamic Programming

---

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the **maximum amount of money you can rob tonight without alerting the police**.

---

## Intuition

At each house, you have exactly **two choices**:

1. **Rob this house** — you cannot rob the previous one, so you take the best amount up to two houses ago + current house value.
2. **Skip this house** — you carry forward the best amount from the previous house.

This is a classic **Dynamic Programming** problem. Instead of storing the entire DP array, we only need to track two rolling variables:

- `adj_1` → max money robbed up to **two houses ago**
- `adj_2` → max money robbed up to the **previous house**

At each step:
```
adj_1, adj_2 = adj_2, max(adj_2, adj_1 + current_num)
```

This gives us an optimal **O(1) space** solution.

---

## Solution

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        adj_1 = 0
        adj_2 = 0
        for num in nums:
            adj_1, adj_2 = adj_2, max(adj_2, adj_1 + num)
        return adj_2
```

---

## Full Example Walkthrough

**Input:** `nums = [2, 7, 9, 3, 1]`

| Step (num) | adj_1 (before) | adj_2 (before) | adj_1 (after) | adj_2 (after)       |
|------------|----------------|----------------|---------------|---------------------|
| num = 2    | 0              | 0              | 0             | max(0, 0+2) = **2** |
| num = 7    | 0              | 2              | 2             | max(2, 0+7) = **7** |
| num = 9    | 2              | 7              | 7             | max(7, 2+9) = **11**|
| num = 3    | 7              | 11             | 11            | max(11, 7+3) = **11**|
| num = 1    | 11             | 11             | 11            | max(11, 11+1) = **12**|

**Output: `12`**

> Rob house 1 (`2`) + house 3 (`9`) + house 5 (`1`) = **12** ✅

---

## Time Complexity

| Complexity | Value |
|------------|-------|
| Time       | O(n)  |
| Space      | O(1)  |

- **Time — O(n):** We iterate through `nums` exactly once. Each step is O(1) work.
- **Space — O(1):** Only two variables (`adj_1`, `adj_2`) are used regardless of input size.

---

## Edge Cases

| Input         | Output | Reason                          |
|---------------|--------|---------------------------------|
| `[]`          | `0`    | Empty array, loop never runs    |
| `[5]`         | `5`    | Only one house                  |
| `[3, 10]`     | `10`   | Rob the richer of the two       |
| `[4, 4, 4, 4]`| `8`    | Rob alternating houses (4+4)    |

---

## Summary

| Property         | Value                            |
|------------------|----------------------------------|
| Time Complexity  | O(n)                             |
| Space Complexity | O(1)                             |
| Approach         | Dynamic Programming (Space Optimized) |
