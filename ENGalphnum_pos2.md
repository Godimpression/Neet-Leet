# Sort Letters and Digits Separately (Optimized)

**Difficulty:** Medium | **Topic:** String, Sorting, Hash Map, Counter

---

## Problem Statement

Given a string `inputStr` containing **letters**, **digits**, and possibly **special characters**, return a new string where:

- All **digits** are sorted among themselves
- All **letters** are sorted among themselves
- The **positions** of digits and letters remain the **same** as in the original string
- **Special characters** are ignored (dropped from output)

**Example:**
```
Input:  "DS1E4T32"
Output: "DE1S2T34"
```

**Explanation:**
```
Original:  D  S  1  E  4  T  3  2
Letters:   D  S     E     T       → sorted → D E S T
Digits:          1     4     3  2 → sorted → 1 2 3 4

Place back at original positions:
Result:    D  E  1  S  2  T  3  4  ✅
```

---

## Intuition 👶

Imagine you have a bag of **red marbles (letters)** and **blue marbles (digits)** mixed together in a line.

**Step 1:** Count how many of each marble you have
```
Red:  D=1, S=1, E=1, T=1
Blue: 1=1, 2=1, 3=1, 4=1
```

**Step 2:** Sort each group alphabetically/numerically
```
Red sorted:  D → E → S → T
Blue sorted: 1 → 2 → 3 → 4
```

**Step 3:** Walk the original line — wherever there was a red marble, place the next sorted red. Wherever there was a blue marble, place the next sorted blue.

> Instead of storing every single marble, we just count them — much more efficient for repeated characters! 🎯

---

## Why Counter Instead of a List?

### The Naive Way (list):
```python
# Store every character
nums = ['1', '4', '3', '2']
nums = sorted(nums)  # sort every time → O(n² log n) 🐢
```

### The Smart Way (Counter):
```python
# Store only unique chars + their frequency
digit_map = Counter({'1':1, '2':1, '3':1, '4':1})
digit_items = sorted(digit_map.items())  # sort ONCE → O(n log n) 🚀
```

For a string like `"AAABBBCCC111222"`:
- List stores 9 letters + 6 digits = 15 entries, sorts repeatedly
- Counter stores only 3 unique letters + 3 unique digits = 6 entries, sorts once ✅

---

## Approach — Step by Step

### Step 1: Count frequencies

```python
letter_map = Counter()
digit_map  = Counter()

for c in inputStr:
    if c.isalpha():
        letter_map[c] += 1
    elif c.isdigit():
        digit_map[c] += 1
    # special characters → ignored
```

For `"DS1E4T32"`:
```
letter_map = {'D':1, 'S':1, 'E':1, 'T':1}
digit_map  = {'1':1, '4':1, '3':1, '2':1}
```

---

### Step 2: Sort unique characters once

```python
letter_items = sorted(letter_map.items())
digit_items  = sorted(digit_map.items())
```

```
letter_items = [('D',1), ('E',1), ('S',1), ('T',1)]
digit_items  = [('1',1), ('2',1), ('3',1), ('4',1)]
```

Sorting is done **once** here — not inside the loop! ✅

---

### Step 3: Rebuild using index pointers

```python
letter_index = 0
digit_index  = 0

for c in inputStr:
    if c.isalpha():
        char, count = letter_items[letter_index]
        result.append(char)
        letter_map[char] -= 1
        if letter_map[char] == 0:
            letter_index += 1   # move to next unique letter
    elif c.isdigit():
        char, count = digit_items[digit_index]
        result.append(char)
        digit_map[char] -= 1
        if digit_map[char] == 0:
            digit_index += 1    # move to next unique digit
    # special chars → skip
```

---

## Full Trace Table

**Input:** `"DS1E4T32"`

### Step 1 & 2 result:
```
letter_items = [('D',1), ('E',1), ('S',1), ('T',1)]
digit_items  = [('1',1), ('2',1), ('3',1), ('4',1)]
```

### Step 3 rebuild:

| Char | Type | Placed | letter_index | digit_index | result so far |
|------|------|--------|-------------|-------------|---------------|
| D | Letter | D | 0→1 | 0 | [D] |
| S | Letter | E | 1→2 | 0 | [D,E] |
| 1 | Digit | 1 | 2 | 0→1 | [D,E,1] |
| E | Letter | S | 2→3 | 1 | [D,E,1,S] |
| 4 | Digit | 2 | 3 | 1→2 | [D,E,1,S,2] |
| T | Letter | T | 3→4 | 2 | [D,E,1,S,2,T] |
| 3 | Digit | 3 | 4 | 2→3 | [D,E,1,S,2,T,3] |
| 2 | Digit | 4 | 4 | 3→4 | [D,E,1,S,2,T,3,4] |

**Output:** `"DE1S2T34"` ✅

---


## Time Complexity — O(n)

| Part | Cost | Why |
|------|------|-----|
| Step 1: Count loop | O(n) | Single pass through string |
| Step 2: Sort letters | O(4 log 4) = **O(1)** | At most 26 unique letters |
| Step 2: Sort digits | O(4 log 4) = **O(1)** | At most 10 unique digits |
| Step 3: Rebuild loop | O(n) | Single pass through string |
| `"".join(result)` | O(n) | Build final string |
| **Total** | **O(n)** | Sorting is constant! ✅ |

> 🔥 Key insight: Since there are only **4 letters** and **4 digits** possible, sorting them is always **O(1)** — it never grows with input size!

---

## Space Complexity — O(n)

| Structure | Space |
|-----------|-------|
| `letter_map` Counter | O(4) = O(1) |
| `digit_map` Counter | O(4) = O(1) |
| `letter_items` / `digit_items` | O(1) |
| `result` list | O(n) |
| **Total** | **O(n)** |

Only the output `result` scales with input size.

---

## Comparison with Naive Approach

| | Naive (list + sort in loop) | This Code (Counter) |
|---|---|---|
| Time | O(n² log n) 🐢 | **O(n)** 🚀 |
| Space | O(n) | O(n) |
| Special chars | ❌ Mixed with letters | ✅ Safely ignored |
| Repeated chars | Slow (re-sorts every time) | ✅ Counted efficiently |
| Sorting | Inside loop (n times) | Once, outside loop |

---

## Edge Cases

| Input | Output | Reason |
|-------|--------|--------|
| `""` | `""` | Empty string, nothing to process |
| `"abc"` | `"abc"` | All letters, sorted in place |
| `"321"` | `"123"` | All digits, sorted in place |
| `"a@b!1"` | `"ab1"` | Special chars dropped |
| `"AABB12"` | `"AABB12"` | Repeated chars handled via count |
| `"bA1"` | `"Ab1"` | Uppercase before lowercase (ASCII order) |

---

## Summary

| Property | Value |
|----------|-------|
| Time Complexity | O(n) |
| Space Complexity | O(n) |
| Key Data Structure | Counter (Hash Map) |
| Sorting cost | O(1) — bounded by alphabet size |
| Special chars | Ignored/dropped |
| Key Insight | Only 6 letters + 2 digits exist → sorting is always constant |
