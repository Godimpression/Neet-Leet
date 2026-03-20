+# 78. Subsets

**Difficulty:** Medium | **Topic:** Array, Backtracking, Bit Manipulation

---

## Problem Statement

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**
```
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

**Example 2:**
```
Input:  nums = [0]
Output: [[], [0]]
```

---

## Baby Explanation 👶

Imagine you have 3 toppings for a pizza: **Cheese, Pepperoni, Mushroom**

You can make a pizza with:
- Nothing on it           → []
- Just Cheese             → [Cheese]
- Just Pepperoni          → [Pepperoni]
- Just Mushroom           → [Mushroom]
- Cheese + Pepperoni      → [Cheese, Pepperoni]
- Cheese + Mushroom       → [Cheese, Mushroom]
- Pepperoni + Mushroom    → [Pepperoni, Mushroom]
- All three               → [Cheese, Pepperoni, Mushroom]

That's **8 combinations** — those are your subsets!

> For any list of `n` items → there are always **2ⁿ** subsets
> Because for EACH item you have 2 choices: **include it or don't** ✅

---

## Intuition

At every element, you make a **binary decision**:
```
Include it? YES or NO
```

Think of it as a decision tree:

```
                    []
                /        \
           [1]              []
          /    \           /    \
       [1,2]  [1]       [2]     []
       /  \   / \      / \    / \
  [1,2,3][1,2][1,3][1][2,3][2][3][]
```

Every path from root to leaf = one subset ✅

---

## Approach — Backtracking

1. Start with an empty subset `[]`
2. At each step, decide to **include** or **skip** the current element
3. Once you've made a decision for all elements → save that subset
4. **Backtrack** → undo the last decision and try the other option

```
nums = [1, 2, 3]

Start with [] → add to result
Take 1 → [1] → add to result
  Take 2 → [1,2] → add to result
    Take 3 → [1,2,3] → add to result ✅
    Skip 3 → backtrack
  Skip 2 → backtrack
  Take 3 → [1,3] → add to result ✅
  Skip 3 → backtrack
Skip 1 → backtrack
Take 2 → [2] → add to result
  Take 3 → [2,3] → add to result ✅
  Skip 3 → backtrack
Skip 2 → backtrack
Take 3 → [3] → add to result ✅
```

---

## Solution

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            # Every state of current is a valid subset
            result.append(current[:])

            for i in range(start, len(nums)):
                # Include nums[i]
                current.append(nums[i])
                # Recurse with next elements
                backtrack(i + 1, current)
                # Backtrack — undo the choice
                current.pop()

        backtrack(0, [])
        return result
```

## Step by Step Walkthrough

**Input:** `nums = [1, 2, 3]`

| Step | Action | current | result so far |
|------|--------|---------|---------------|
| 1 | Start | [] | [[]] |
| 2 | Add 1 | [1] | [[], [1]] |
| 3 | Add 2 | [1, 2] | [[], [1], [1,2]] |
| 4 | Add 3 | [1, 2, 3] | [[], [1], [1,2], [1,2,3]] |
| 5 | Pop 3 (backtrack) | [1, 2] | same |
| 6 | Pop 2 (backtrack) | [1] | same |
| 7 | Add 3 | [1, 3] | [..., [1,3]] |
| 8 | Pop 3 (backtrack) | [1] | same |
| 9 | Pop 1 (backtrack) | [] | same |
| 10 | Add 2 | [2] | [..., [2]] |
| 11 | Add 3 | [2, 3] | [..., [2,3]] |
| 12 | Pop 3 (backtrack) | [2] | same |
| 13 | Pop 2 (backtrack) | [] | same |
| 14 | Add 3 | [3] | [..., [3]] |

**Final Output:**
```
[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
```

---

## Why `current[:]`?

```python
result.append(current[:])   # ✅ correct — appends a COPY
result.append(current)      # ❌ wrong  — appends a REFERENCE
```

If you append `current` directly, every entry in result points to the **same list**.
When you backtrack and modify `current`, all entries change too!

`current[:]` creates a **snapshot copy** at that moment. 📸

---

## Time Complexity — O(n × 2ⁿ)

| Part | Cost |
|---|---|
| Number of subsets | 2ⁿ |
| Copying each subset into result | O(n) per subset |
| **Total** | **O(n × 2ⁿ)** |

For `n = 3`:
- 2³ = **8 subsets**
- Each copy takes up to 3 operations
- Total ≈ **24 operations**

> This is the **best possible** time complexity for this problem — you can't do better because you MUST generate all 2ⁿ subsets ✅

---

## Space Complexity — O(n × 2ⁿ)

| Part | Space |
|---|---|
| Storing all subsets in result | O(n × 2ⁿ) |
| Recursion call stack depth | O(n) |
| current list at any point | O(n) |
| **Total** | **O(n × 2ⁿ)** |

The dominant cost is storing all the subsets in the output.

---

## Edge Cases

| Input | Output | Reason |
|---|---|---|
| `nums = []` | `[[]]` | Only the empty subset exists |
| `nums = [1]` | `[[], [1]]` | Include or exclude the one element |
| `nums = [1,2]` | `[[], [1], [1,2], [2]]` | 2² = 4 subsets |

---

## Key Takeaways

- For `n` elements → always **2ⁿ** subsets (include/exclude each)
- Backtracking = **try → recurse → undo**
- Always copy with `current[:]` not `current`
- The recursion depth never exceeds `n`

---

## Summary

| Property | Value |
|---|---|
| Time Complexity | O(n × 2ⁿ) |
| Space Complexity | O(n × 2ⁿ) |
| Approach | Backtracking |
| Key Insight | Each element has 2 choices: include or skip |
| Total subsets for n elements | 2ⁿ |
