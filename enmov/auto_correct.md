# Autocorrect: One Character Different

## Problem
Given a dictionary of words, implement an autocorrect system that:
1. Returns the word immediately if it's an **exact match**.
2. Returns a dictionary word if it differs by **exactly one character** (same length, one mismatch).
3. Returns the original word unchanged if no match is found.

## Strategy

| Step | Description | Complexity |
|------|-------------|------------|
| **Exact Match** | Check if the word exists in the dictionary set | O(1) |
| **Filtered Search** | Only compare words with the same length | Skips most candidates |
| **Mismatch Pointer** | Compare char-by-char; bail early at 2+ mismatches | O(L) per candidate |

## Implementation

```python
class Autocorrect:
    def __init__(self, words):
        # Store as a set for O(1) exact match lookups
        self.dictionary = set(words)

    def correct(self, word):
        # 1. Exact match check
        if word in self.dictionary:
            return word

        # 2. Look for a "one character different" match
        for dict_word in self.dictionary:
            if len(dict_word) == len(word):
                mismatches = 0
                for i in range(len(word)):
                    if word[i] != dict_word[i]:
                        mismatches += 1
                    # Optimization: stop if we already found 2+ differences
                    if mismatches > 1:
                        break
                if mismatches == 1:
                    return dict_word

        # 3. No match found, return the original word
        return word
```

## Usage

```python
corrector = Autocorrect(["apple", "pear", "orange"])

corrector.correct("apply")   # → "apple"  (1 mismatch: y→e)
corrector.correct("apples")  # → "apples" (different length, no match)
corrector.correct("bear")    # → "pear"   (1 mismatch: b→p)
```

## Performance

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(N × L) worst case — N = dictionary size, L = word length |
| **Space Complexity** | O(N × L) to store the dictionary |

## Why It Works

- **Efficiency** — The length check (`len(dict_word) == len(word)`) eliminates most candidates immediately.
- **Correctness** — Words with 2+ mismatches are rejected via the early-exit optimization.
- **Storage** — A `set` provides O(1) exact-match lookups, scaling well for large dictionaries.

## Potential Optimization

Group dictionary words by length in a `dict[int, list[str]]` so the filtered search only iterates over same-length words without scanning the entire dictionary.
