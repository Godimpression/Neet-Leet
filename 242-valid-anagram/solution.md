# Valid Anagram (LeetCode 242) — Quick README

## Problem
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, else `False`.

An anagram means both strings contain the **same characters with the same frequencies**, but possibly in different orders.

### Example
- `s = "abcd"`, `t = "cdab"` → `True`
- `s = "rat"`, `t = "car"` → `False`

---

## How `Counter` Works
Python’s `Counter` counts items and returns a dictionary-like object.

```python
from collections import Counter

Counter("aabfffr")
# Counter({'f': 3, 'a': 2, 'b': 1, 'r': 1})
```

It means:
- `'a'` appears 2 times
- `'f'` appears 3 times
- `'b'` appears 1 time
- `'r'` appears 1 time

---

## Correct Solution (Using Counter)
If two strings are anagrams, their counters are equal:

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

### Why this works
- `Counter(s)` builds a frequency table for `s`
- `Counter(t)` builds a frequency table for `t`
- Equality checks **every character count**

---

## Common Mistake (Why Your Loop Was Wrong)
This pattern returns too early:

```python
for ch in s:
    if s == t:
        return True
    else:
        return False
```

Because it returns `False` on the *first iteration*.

---

## Alternative Solution (Frequency Array) — O(N)
If the strings are only lowercase English letters (`a`–`z`), you can use a fixed array of size 26:

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(x == 0 for x in count)
```

---

## Complexity
- `Counter` approach: **O(N)** time, **O(1)** space for fixed alphabet (or O(K) for unique chars)
- Sorting approach: **O(N log N)** time

---

## Tip
When you see “anagram”, think:
- **same counts** → use `Counter` or frequency array
