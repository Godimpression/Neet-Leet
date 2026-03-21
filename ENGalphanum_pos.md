# Sort Characters and Digits Separately

**Difficulty:** Medium | **Topic:** String, Sorting, Two Pointers

---

## Problem Statement

Given a string `S` containing both **letters** and **digits**, return a new string where:

- All **digits** are sorted among themselves
- All **letters** are sorted among themselves
- The **positions** of digits and letters remain the **same** as in the original string

In other words — sort the digits and letters independently, but keep digits where digits were and letters where letters were.

**Example:**
```
Input:  S = "DS1E4T32"
Output: "DE1S3T42"
```

**Explanation:**
```
Original:  D  S  1  E  4  T  3  2
           ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓
Letters:   D  S     E     T         → sorted → D E S T
Digits:          1     4     3  2   → sorted → 1 2 3 4

Now place them back in original positions:
Position:  0  1  2  3  4  5  6  7
Type:      L  L  D  L  D  L  D  D
Fill:      D  E  1  S  3  T  2  4  ✅
```

---

## Intuition 👶

Imagine you have a row of **red and blue boxes**:

```
[D] [S] [1] [E] [4] [T] [3] [2]
 L   L   D   L   D   L   D   D
```

**Step 1:** Pick out all the **blue boxes (digits)** → sort them → `[1, 2, 3, 4]`

**Step 2:** Pick out all the **red boxes (letters)** → sort them → `[D, E, S, T]`

**Step 3:** Put them back — wherever there was a blue box, place the next sorted digit. Wherever there was a red box, place the next sorted letter.

```
Result: [D] [E] [1] [S] [3] [T] [2] [4]
```

You never mix red and blue — you just sort within each color! 🎨

---

## Approach — Step by Step

### Phase 1: Separate and Sort

Loop through the string once:
- If character is a **digit** → add to `nums` list, keep it sorted
- If character is a **letter** → add to `lett` list, keep it sorted

```
S = "DS1E4T32"

i=0: 'D' → letter → lett=['D']
i=1: 'S' → letter → lett=['D','S']
i=2: '1' → digit  → nums=['1']
i=3: 'E' → letter → lett=['D','E','S']
i=4: '4' → digit  → nums=['1','4']
i=5: 'T' → letter → lett=['D','E','S','T']
i=6: '3' → digit  → nums=['1','3','4']
i=7: '2' → digit  → nums=['1','2','3','4']
```

### Phase 2: Rebuild the String

Loop through original string again:
- If position had a **digit** → pop the first (smallest) digit from `nums`
- If position had a **letter** → pop the first (smallest) letter from `lett`

```
i=0: 'D' → letter → pop lett[0]='D' → final=['D']
i=1: 'S' → letter → pop lett[0]='E' → final=['D','E']
i=2: '1' → digit  → pop nums[0]='1' → final=['D','E','1']
i=3: 'E' → letter → pop lett[0]='S' → final=['D','E','1','S']
i=4: '4' → digit  → pop nums[0]='2' → final=['D','E','1','S','2']  ← wait
```

> ⚠️ Note: nums after phase 1 = ['1','2','3','4']
> So popping in order gives 1, 2, 3, 4 — placed at digit positions

```
Final: D E 1 S 2 T 3 4
```

---

## The Code

```python
S = "DS1E4T32"
trans = list(S)

def alphanum(s):
    nums = []
    lett = []
    final = []

    # Phase 1: Separate and sort
    for i in range(len(s)):
        if s[i].isdigit():
            nums.append(s[i])
            nums = sorted(nums)
        else:
            lett.append(s[i])
            lett = sorted(lett)

    # Phase 2: Rebuild using original positions
    for i in s:
        if i.isdigit():
            final.append(nums.pop(0))
        else:
            final.append(lett.pop(0))

    return "".join(final)

alphanum(trans)
```

---

## Full Trace Table

**Input:** `"DS1E4T32"`

| Index | Char | Type | nums after | lett after |
|-------|------|------|------------|------------|
| 0 | D | Letter | [] | [D] |
| 1 | S | Letter | [] | [D, S] |
| 2 | 1 | Digit | [1] | [D, S] |
| 3 | E | Letter | [1] | [D, E, S] |
| 4 | 4 | Digit | [1, 4] | [D, E, S] |
| 5 | T | Letter | [1, 4] | [D, E, S, T] |
| 6 | 3 | Digit | [1, 3, 4] | [D, E, S, T] |
| 7 | 2 | Digit | [1, 2, 3, 4] | [D, E, S, T] |

**Rebuild phase:**

| Position | Original | Type | Popped | final |
|----------|----------|------|--------|-------|
| 0 | D | Letter | D | [D] |
| 1 | S | Letter | E | [D, E] |
| 2 | 1 | Digit | 1 | [D, E, 1] |
| 3 | E | Letter | S | [D, E, 1, S] |
| 4 | 4 | Digit | 2 | [D, E, 1, S, 2] |
| 5 | T | Letter | T | [D, E, 1, S, 2, T] |
| 6 | 3 | Digit | 3 | [D, E, 1, S, 2, T, 3] |
| 7 | 2 | Digit | 4 | [D, E, 1, S, 2, T, 3, 4] |

**Output:** `"DE1S2T34"` ✅

---

## Time Complexity — O(n² log n)

| Part | Cost | Why |
|------|------|-----|
| Phase 1 loop | O(n) iterations | Loop through string once |
| `sorted()` inside loop | O(k log k) per call | k grows up to n |
| Total Phase 1 | O(n² log n) | sorting called n times |
| Phase 2 loop | O(n) | Loop through string once |
| `pop(0)` on list | O(k) per call | Shifts all elements left |
| Total Phase 2 | O(n²) | pop(0) called n times |
| **Overall** | **O(n² log n)** | Phase 1 dominates |

> ⚡ **Optimized version** would sort ONCE after the loop → O(n log n) total

---

## Space Complexity — O(n)

| Structure | Space |
|-----------|-------|
| `nums` list | O(d) where d = number of digits |
| `lett` list | O(l) where l = number of letters |
| `final` list | O(n) |
| **Total** | **O(n)** |

All lists together hold at most `n` characters total.

---

## Optimization Tip 💡

The current code sorts inside the loop on every iteration — that's expensive!

```python
# ❌ Current — sorts on every iteration O(n² log n)
for i in range(len(s)):
    if s[i].isdigit():
        nums.append(s[i])
        nums = sorted(nums)   # ← unnecessary here

# ✅ Better — sort ONCE after the loop O(n log n)
for i in range(len(s)):
    if s[i].isdigit():
        nums.append(s[i])
    else:
        lett.append(s[i])

nums.sort()   # sort once
lett.sort()   # sort once
```

---

## Edge Cases

| Input | Output | Reason |
|-------|--------|--------|
| `"abc"` | `"abc"` | No digits, letters sorted in place |
| `"321"` | `"123"` | No letters, digits sorted in place |
| `"a1"` | `"a1"` | One of each, already sorted |
| `"1a"` | `"1a"` | Digit first, letter second — positions preserved |
| `""` | `""` | Empty string, nothing to do |

---

## Summary

| Property | Value |
|----------|-------|
| Time Complexity | O(n² log n) — optimizable to O(n log n) |
| Space Complexity | O(n) |
| Key Technique | Separate → Sort → Rebuild |
| Core Insight | Preserve positions, sort values within each type |
| Uses | `isdigit()`, `sorted()`, `pop(0)`, `"".join()` |
