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
