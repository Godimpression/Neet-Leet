# 2109. Adding Spaces to a String

**Difficulty:** Medium | **Topic:** String, Array, Two Pointers

---

## Problem Statement

You are given a **0-indexed** string `s` and a **0-indexed** integer array `spaces` that describes the indices in the original string where spaces will be added.

- Each space should be inserted **before** the character at the given index.

Return the modified string **after** the spaces have been added.

**Example:**
```
Input:  s = "LeetcodeHelpsMeLearn", spaces = [8, 13, 15]
Output: "Leetcode Helps Me Learn"
```

---

## Intuition

Instead of inserting spaces one by one into the string (which is expensive due to string immutation), we:

1. **Slice** the string between each space index
2. **Collect** all chunks into a list
3. **Join** everything at the end with `"".join()`

This avoids repeatedly creating new strings and is much more efficient.

Think of it like cutting a ribbon at marked positions and laying the pieces down with gaps between them ✂️

---

## Approach — Step by Step

Given:
```
s      = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
```

We maintain a `last_ind` pointer that tracks where the last slice ended.

| Iteration | last_ind | spaces[i] | Chunk sliced     | Appended       |
|-----------|----------|-----------|------------------|----------------|
| i = 0     | 0        | 8         | s[0:8] = "Leetcode" | "Leetcode", " " |
| i = 1     | 8        | 13        | s[8:13] = "Helps"   | "Helps", " "    |
| i = 2     | 13       | 15        | s[13:15] = "Me"     | "Me", " "       |
| End       | 15       | —         | s[15:] = "Learn"    | "Learn"         |

Final join:
```
"Leetcode" + " " + "Helps" + " " + "Me" + " " + "Learn"
= "Leetcode Helps Me Learn" ✅
```

---

## Solution

```python
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        splits = []
        last_ind = 0

        for i in range(len(spaces)):
            # Slice from the last space to the current space
            word_chunk = s[last_ind:spaces[i]]
            splits.append(word_chunk)
            splits.append(" ")
            last_ind = spaces[i]

        # Grab everything from the last space to the end of the string
        splits.append(s[last_ind:])

        return "".join(splits)
```

---

## Why Not Just Insert Directly?

You might think to do this:

```python
# ❌ Naive approach — very slow
for i, space in enumerate(spaces):
    s = s[:space + i] + " " + s[space + i:]
return s
```

**Problem:** Strings in Python are **immutable**. Every `+` creates a **brand new string**, copying all characters each time.

- For `n` spaces on a string of length `L` → **O(n × L)** time 🐢
- Our approach using a list + join → **O(n + L)** time 🚀

---

## Complexity Analysis

### ⏱️ Time Complexity — O(n + L)

| Part | Cost |
|---|---|
| Iterating through `spaces` array | O(n) |
| Slicing string chunks | O(L) total across all slices |
| `"".join(splits)` | O(L) |
| **Total** | **O(n + L)** |

Where:
- `n` = length of `spaces` array
- `L` = length of string `s`

---

### 🗂️ Space Complexity — O(n + L)

| Part | Space |
|---|---|
| `splits` list stores all chunks + spaces | O(L + n) |
| Output string | O(L + n) |
| **Total** | **O(n + L)** |

We store all the pieces in a list before joining — necessary to avoid the expensive repeated string concatenation.

---

## Edge Cases

| Input | Output | Reason |
|---|---|---|
| `s = "a"`, `spaces = []` | `"a"` | No spaces to add, loop never runs |
| `s = "ab"`, `spaces = [1]` | `"a b"` | Space inserted before index 1 |
| `spaces` at start `[0]` | `" ab..."` | Empty chunk at start, space prepended |
| `spaces` at last index | `"...a b"` | Last char gets a space before it |

---

## Summary

| Property | Value |
|---|---|
| Time Complexity | O(n + L) |
| Space Complexity | O(n + L) |
| Key Technique | Slice + List + Join |
| Why not direct insert? | String immutability makes it O(n × L) |
| Approach | Two pointer / sliding window on indices |
