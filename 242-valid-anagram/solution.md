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


---

# Anagram Problem — ASCII vs Unicode Explained

---

## What is an Anagram?
Two strings are anagrams if they contain the **same characters with the same frequencies**, in any order.

- `"silent"` and `"listen"` → anagrams ✅
- `"rat"` and `"car"` → not anagrams ❌

---

## APPROACH 1: ASCII (Fixed Array of Size 26)

### When to use it
Only when your strings contain **lowercase English letters** (a–z).

### The Code

```python
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    count = [0] * 26  # 26 zeros, one per letter

    for c in s1:
        count[ord(c) - ord('a')] += 1  # increment

    for c in s2:
        count[ord(c) - ord('a')] -= 1  # decrement

    return all(x == 0 for x in count)
```

---

### Step 1: What is `[0] * 26`?
Creates a list of 26 zeros — one slot for each letter of the alphabet:

```
Index:  0   1   2   3   4  ...  25
Letter: a   b   c   d   e  ...  z
Value:  0   0   0   0   0  ...  0
```

Think of it as 26 empty boxes, one per letter.

---

### Step 2: What is `ord()`?
`ord()` converts a character to its ASCII number:

```
ord('a') = 97
ord('b') = 98
ord('c') = 99
...
ord('z') = 122
```

So `ord(c) - ord('a')` gives the index in the array:

```
ord('a') - ord('a') = 0   → index 0 (box for 'a')
ord('b') - ord('a') = 1   → index 1 (box for 'b')
ord('c') - ord('a') = 2   → index 2 (box for 'c')
ord('z') - ord('a') = 25  → index 25 (box for 'z')
```

---

### Step 3: Full Walkthrough — s1 = "abc", s2 = "cab"

Start:
```
count = [0, 0, 0, 0, 0, ... 0]   (26 zeros)
```

Loop 1 — go through s1 = "abc" (increment):
- See 'a' → index 0 → count[0] += 1
- See 'b' → index 1 → count[1] += 1
- See 'c' → index 2 → count[2] += 1

```
Index:  0   1   2   3 ... 25
        1   1   1   0 ... 0
        ↑   ↑   ↑
        a   b   c
```

Loop 2 — go through s2 = "cab" (decrement):
- See 'c' → index 2 → count[2] -= 1
- See 'a' → index 0 → count[0] -= 1
- See 'b' → index 1 → count[1] -= 1

```
Index:  0   1   2   3 ... 25
        0   0   0   0 ... 0
```

Final check: all zeros → True ✅ They are anagrams!

---

### What if NOT anagrams? — s1 = "abc", s2 = "xyz"

After loop 1 (s1 = "abc"):
```
a=1, b=1, c=1, rest=0
```

After loop 2 (s2 = "xyz"):
```
a=1, b=1, c=1, x=-1, y=-1, z=-1
```

Not all zeros → False ❌

---

### Why increment then decrement?
Think of it like a balance sheet:
- s1 ADDS to the balance
- s2 TAKES from the balance
- If they are anagrams, everything cancels out to zero

---

### ASCII Memory
- Always uses exactly 26 integer slots
- Space: O(1) — constant, never changes no matter how long the string is

---
---

## APPROACH 2: Unicode (Hash Map / Counter)

### When to use it
When strings can contain **any character** — emojis, Arabic, Chinese, accented letters, symbols, etc.

### Why ASCII approach FAILS for Unicode

Unicode has 140,000+ possible characters.

You cannot do this:
```python
count = [0] * 140000  # ❌ wasteful — most slots will always be empty
```

If your string is just `"hello"`, you'd still allocate 140,000 slots but only use 4 of them.
That is a massive waste of memory.

---

### The Unicode Solution — Hash Map

```python
def are_anagrams_unicode(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}  # empty dictionary — only stores what it sees

    for c in s1:
        count[c] = count.get(c, 0) + 1  # increment

    for c in s2:
        count[c] = count.get(c, 0) - 1  # decrement

    return all(v == 0 for v in count.values())
```

---

### Step-by-Step Walkthrough — s1 = "café", s2 = "éfac"

These strings contain `é` — a Unicode character (not in basic ASCII).

Start:
```
count = {}   (empty dictionary)
```

Loop 1 — go through s1 = "café" (increment):
- See 'c' → count = {'c': 1}
- See 'a' → count = {'c': 1, 'a': 1}
- See 'f' → count = {'c': 1, 'a': 1, 'f': 1}
- See 'é' → count = {'c': 1, 'a': 1, 'f': 1, 'é': 1}

Loop 2 — go through s2 = "éfac" (decrement):
- See 'é' → count = {'c': 1, 'a': 1, 'f': 1, 'é': 0}
- See 'f' → count = {'c': 1, 'a': 1, 'f': 0, 'é': 0}
- See 'a' → count = {'c': 1, 'a': 0, 'f': 0, 'é': 0}
- See 'c' → count = {'c': 0, 'a': 0, 'f': 0, 'é': 0}

Final check: all zeros → True ✅ They are anagrams!

---

### What does `count.get(c, 0)` mean?
It means: "get the value for key c, but if c doesn't exist yet, return 0 instead of crashing."

This is the dictionary equivalent of what defaultdict(int) does automatically.

---

### Unicode with Counter (Cleanest Version)

```python
from collections import Counter

def are_anagrams_unicode(s1, s2):
    return Counter(s1) == Counter(s2)
```

Counter works with ANY character — ASCII, Unicode, emojis, everything.

Example:
```python
Counter("café")  →  {'c': 1, 'a': 1, 'f': 1, 'é': 1}
Counter("éfac")  →  {'é': 1, 'f': 1, 'a': 1, 'c': 1}

# Equal → True ✅
```

---

### Unicode Memory
- Only stores characters that ACTUALLY APPEAR in the string
- Space: O(K) where K = number of unique characters in the input
- If string is "hello" → only 4 entries stored, not 140,000

---
---

## ASCII vs Unicode — Side by Side

| Feature              | ASCII (Fixed Array)         | Unicode (Hash Map)              |
|----------------------|-----------------------------|---------------------------------|
| Characters supported | a–z only (26 letters)       | Any character (140,000+)        |
| Data structure       | `[0] * 26`                  | `{}` dictionary / `Counter`     |
| Memory used          | Always 26 slots (O(1))      | Only seen characters (O(K))     |
| Speed                | Slightly faster (array)     | Slightly slower (hashing)       |
| Works with emojis?   | ❌ No                        | ✅ Yes                           |
| Works with Arabic?   | ❌ No                        | ✅ Yes                           |
| Interview use        | Shows low-level knowledge   | Shows Unicode awareness         |

---

## Key Insight
- ASCII fixed array = fast and lean, but LIMITED
- Unicode hash map = flexible and dynamic, stores ONLY what it sees
- Counter = the cleanest Python shortcut for both cases

---

## Quick Interview Tip
If an interviewer asks:
> "What if the input contains Unicode characters?"

Say:
> "I would replace the fixed array with a hash map or Counter,
> because the character set is too large for a fixed array.
> The hash map only stores characters that actually appear,
> so the memory footprint stays proportional to the input,
> not the entire Unicode character set."



