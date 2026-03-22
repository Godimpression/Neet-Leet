# Word Ladder (LeetCode 127) — BFS + Pattern (Wildcard) Graph

This README explains the common high-performance solution shown in the screenshot: **Breadth-First Search (BFS)** over an implicit graph of words, accelerated by a **wildcard pattern → neighbors** map.

## Problem
Given:
- `beginWord` (start)
- `endWord` (target)
- `wordList` (dictionary)

Return the length of the shortest transformation sequence from `beginWord` to `endWord` such that:
- Only **one letter** can change at a time
- Every transformed word must be in `wordList`

If no sequence exists, return `0`.

---

## Intuition

You can view each word as a node in a graph:
- There is an edge between two words if they differ by **exactly 1 letter**.

We need the **shortest path** from `beginWord` to `endWord` → this is exactly what **BFS** is for.

### Why the wildcard pattern trick?
Naively, to find neighbors of a word you might compare it against every word in `wordList` (slow).

Instead, we generate *patterns* by replacing each character with `*`.

Example for `word = "hot"`:
- `*ot`
- `h*t`
- `ho*`

Any two words that share a pattern are neighbors (one letter apart).
So we build a mapping:

- pattern → list of words that match that pattern

Then, from a word, we can generate its patterns and instantly retrieve all neighbors.

---

## Core Idea in the Code

### 1) Early exit
If `endWord` is not in `wordList`, it’s impossible:

```python
if endWord not in wordList:
    return 0
```

### 2) Build the wildcard adjacency map
Use a dictionary like `defaultdict(list)`:

```python
nei = collections.defaultdict(list)
wordList.append(beginWord)

for word in wordList:
    for j in range(len(word)):
        pattern = word[:j] + "*" + word[j+1:]
        nei[pattern].append(word)
```

Now, `nei["h*t"]` might contain `["hot", "hit"]`.

### 3) BFS from beginWord
Track visited words to avoid cycles:

```python
visit = set([beginWord])
q = deque([beginWord])
res = 1
```

Process level-by-level. Each BFS “level” means one transformation step.

```python
while q:
    for i in range(len(q)):
        word = q.popleft()
        if word == endWord:
            return res

        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            for neiWord in nei[pattern]:
                if neiWord not in visit:
                    visit.add(neiWord)
                    q.append(neiWord)

    res += 1

return 0
```

---

## Full Example Walkthrough

### Example
```
beginWord = "hit"
endWord   = "cog"
wordList  = ["hot","dot","dog","lot","log","cog"]
```

### Step A — Build patterns (some examples)
For `"hot"`:
- `*ot` → ["hot", "dot", "lot"]
- `h*t` → ["hot"]
- `ho*` → ["hot"]

For `"dot"`:
- `d*t` → ["dot"]
- `do*` → ["dot", "dog"]
- `*ot` → ["hot", "dot", "lot"]

…and so on.

### Step B — BFS levels
**Level 1** (`res = 1`):
- start: `hit`
- patterns of `hit`: `*it`, `h*t`, `hi*`
- neighbors via `h*t`: `hot`
- queue becomes: [`hot`]

**Level 2** (`res = 2`):
- process `hot`
- neighbors include `dot`, `lot`
- queue: [`dot`, `lot`]

**Level 3** (`res = 3`):
- process `dot` → neighbor `dog`
- process `lot` → neighbor `log`
- queue: [`dog`, `log`]

**Level 4** (`res = 4`):
- process `dog` → neighbor `cog`
- queue: [`cog`, ...]

**Level 5** (`res = 5`):
- pop `cog` == endWord → return `5`

So shortest chain length is:
```
hit → hot → dot → dog → cog
length = 5
```

---

## Time Complexity
Let:
- `N` = number of words in `wordList`
- `L` = length of each word

### Building the pattern map
For each word, we build `L` patterns, each pattern creation is O(L) due to slicing/concatenation.
- **Time**: O(N · L²)
- **Space**: O(N · L) patterns stored, and total word references across lists is O(N · L)

### BFS
Each word is visited at most once.
For each visited word, we generate `L` patterns and iterate its neighbor lists.
Overall, across all patterns, total neighbor traversals are bounded by the size of the map lists.
- **Time** (typical bound used in interviews): O(N · L²)
- **Space**: O(N · L) for map + O(N) for queue/visited

> Many interviewers accept: **O(N · L²)** time and **O(N · L)** space.

---

## Why BFS is Correct
BFS explores transformations in increasing number of steps:
- first all words 1 change away,
- then 2 changes away,
- etc.

The first time we reach `endWord`, it must be the shortest transformation sequence.

---

## Notes / Common Improvements
- You can optionally clear `nei[pattern]` after processing it to reduce repeated scanning of the same neighbor list.
- Another common optimisation is **bidirectional BFS** (from both begin and end), which can be much faster on big inputs.

---

## Reference Implementation (as in screenshot)

```python
import collections
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0
```
