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




# Anagrams (Frequency Map / Counter) — README

## What is an Anagram?
Two strings are **anagrams** if they contain the **same characters with the same frequencies** (counts), in any order.

Examples:
- `"silent"` and `"listen"` → anagrams ✅
- `"rat"` and `"car"` → not anagrams ❌

---

## Big Idea: Compare Character Frequencies (Not Order)
Instead of sorting (which costs \(O(N \log N)\)), we can count letters in each string in \(O(N)\) time.

If the counts match exactly, the strings are anagrams.

---

## Helper-Function Approach (Manual Version of `Counter`)
Think of two functions:

- `are_anagrams(s1, s2)` = the **manager**
- `_to_dict(s)` = the **worker** that builds an "inventory" (frequency map)

### How the two functions connect
Inside `are_anagrams`, we call `_to_dict` twice:

```python
from collections import defaultdict

def _to_dict(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d

def are_anagrams(string1, string2):
    dict1 = _to_dict(string1)  # worker processes string1
    dict2 = _to_dict(string2)  # worker processes string2
    return dict1 == dict2      # manager compares results
```

---

## Why `defaultdict(int)` Helps
Normally, this would crash if the key doesn’t exist yet:

```python
d[c] += 1  # KeyError if c not already in d
```

But `defaultdict(int)` automatically gives missing keys the value `0`.
So the first time you see a letter, `d[letter]` starts at `0`, then becomes `1`.

---

## Step-by-Step Example: How `_to_dict` Works
Input string: `"apple"`

Start:
- `d = {}` (conceptually empty)

Walk through each character:

1. See `'a'` → `d['a']` goes `0 → 1`
   - `{'a': 1}`
2. See `'p'` → `d['p']` goes `0 → 1`
   - `{'a': 1, 'p': 1}`
3. See `'p'` again → `d['p']` goes `1 → 2`
   - `{'a': 1, 'p': 2}`
4. See `'l'` → `0 → 1`
   - `{'a': 1, 'p': 2, 'l': 1}`
5. See `'e'` → `0 → 1`
   - `{'a': 1, 'p': 2, 'l': 1, 'e': 1}`

Return that dictionary.

This is exactly how duplicates are handled: **each repeat increments the count**.

---

## Dictionary Comparison: `dict1 == dict2`
When you do `dict1 == dict2`, Python checks:

1. Same keys?
2. Same values for each key?

Example:
- `"aabb"` → `{'a': 2, 'b': 2}`
- `"abab"` → `{'a': 2, 'b': 2}`

They match → `True` ✅

---

## Early Exit Optimization (Length Check)
If lengths differ, they can’t be anagrams.

```python
def are_anagrams(string1, string2):
    if len(string1) != len(string2):
        return False
    return _to_dict(string1) == _to_dict(string2)
```

This saves time for obvious mismatches.

---

## The `Counter` Shortcut (Cleaner Python)
`Counter` does the same counting for you.

```python
from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)
```

### Example
- `Counter("aabfffr")` → `{'f': 3, 'a': 2, 'b': 1, 'r': 1}`
- `Counter("afbfraf")` → `{'f': 3, 'a': 2, 'b': 1, 'r': 1}`

Equal → anagrams ✅

---

## Handling Capitalization ("Apple" vs "apple")
Decide if your problem is **case-sensitive**.

### Case-insensitive anagram check
Convert both strings to lowercase first:

```python
from collections import Counter

def are_anagrams_case_insensitive(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())
```

Now:
- `"Apple"` and `"apple"` → `True` ✅

---

## Complexity
Let \(N\) be the length of the string.

- Frequency map / Counter:
  - Time: \(O(N)\)
  - Space: \(O(K)\) where \(K\) is number of unique characters (often bounded, e.g., 26 lowercase letters)

- Sorting approach:
  - Time: \(O(N \log N)\)

---

## Quick Interview Notes
- Mention the **length check** first.
- Explain that order doesn’t matter, only **counts**.
- Use `Counter` in Python for clean code, but know how to build a frequency map manually.

