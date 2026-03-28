# Solution 4: Sort + Sweep + Midnight Wrapping — Line by Line

## The Problem It Solves

Banks can wrap past midnight. For example, Tokyo trades from 22:00 to 6:00. A normal sort+sweep would break because 22 > 6. Solution 4 handles this by splitting wrapping banks and orders into two pieces.

---

## The Data Structures

```python
class Order:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

class Bank:
    def __init__(self, name, trading_start, trading_end):
        self.name = name
        self.trading_start = trading_start
        self.trading_end = trading_end
```

These are just containers. `self.start_time` is a number like `10`. `self.name` is a string like `"RBS"`. Nothing fancy — just storing data so we can access it later with the dot notation.

---

## Function 1: `can_trade_monotonic_4` (The Sweep)

This function assumes **no midnight wrapping** — all times go left to right normally. It's the engine that does the actual checking.

```python
def can_trade_monotonic_4(order, sorted_banks):
    current_start = order.start_time
```

**What this does**: Creates a pointer called `current_start`. This tracks "how far have we been covered so far?" We start at the order's start time.

Example: If the order is 10–17, then `current_start = 10`. We need to push this all the way to 17.

---

```python
    for bank in sorted_banks:
```

**What this does**: Loop through every bank, one by one. They're already sorted by start time (smallest first), so we process them left to right on the timeline.

---

```python
        if current_start < bank.trading_start:
            return False
```

**What this does**: "Is there a GAP between where we've been covered and where this bank starts?"

If yes → we're stuck. No bank can fill this gap (because banks are sorted — every bank after this one starts even later). Return False immediately.

Example:
- current_start = 10, bank starts at 12
- Gap from 10 to 12 that nobody covers → **Fail**

---

```python
        if order.end_time <= bank.trading_end:
            return True
```

**What this does**: "Does this bank cover all the way to the order's end (or beyond)?"

If yes → we're done! The entire order is covered. Return True.

Example:
- Order ends at 17, bank ends at 20
- 17 ≤ 20 → this bank covers the rest → **Success**

---

```python
        if current_start < bank.trading_end:
            current_start = bank.trading_end
```

**What this does**: "This bank doesn't fully cover the order, but it pushes us forward."

Move `current_start` to this bank's end time, then continue to the next bank.

Example:
- current_start = 10, bank is [9–16]
- Order ends at 17, so 17 ≤ 16 is False (not fully covered yet)
- But 10 < 16, so push current_start → 16
- Now we need another bank to cover 16–17

---

```python
    return False
```

**What this does**: We went through all banks and never fully covered the order. Return False.

---

### Full Walkthrough of `can_trade_monotonic_4`

Order: 10–17. Sorted banks: [2–7], [9–16], [11–17], [14–20]

```
current_start = 10

Bank [2-7]:
  10 < 2?  No  (no gap)
  17 <= 7? No  (doesn't cover the end)
  10 < 7?  No  (can't push us forward either — we're already past 7)
  → Skip this bank, it's useless for our order

Bank [9-16]:
  10 < 9?  No  (no gap)
  17 <= 16? No (doesn't cover the end)
  10 < 16? YES → current_start = 16
  → We're now covered up to 16. Need 16–17 still.

Bank [11-17]:
  16 < 11? No  (no gap)
  17 <= 17? YES → return True! ✅
  → This bank covers the rest!
```

---

## Function 2: `can_trade_4` (The Orchestrator)

This function handles all the midnight wrapping logic, then hands off to `can_trade_monotonic_4` for the actual check.

### Step 1: Split Midnight-Wrapping Banks

```python
def can_trade_4(order, banks):
    expanded = []
    for bank in banks:
        if bank.trading_end < bank.trading_start:
            expanded.append(Bank(bank.name, 0, bank.trading_end))
            expanded.append(Bank(bank.name, bank.trading_start, 24))
        else:
            expanded.append(bank)
```

**What this does**: If a bank wraps past midnight (end < start), split it into two normal banks.

Example:
- Tokyo trades 22:00–6:00 → `trading_end (6) < trading_start (22)` → wraps!
- Split into: [0–6] and [22–24]
- Now both pieces go left to right normally

If a bank doesn't wrap (like RBS 9–16), just add it as-is.

```
Before: Tokyo [22-6]
After:  Tokyo [0-6] + Tokyo [22-24]
```

---

### Step 2: Sort Everything

```python
    expanded.sort(key=lambda b: (b.trading_start, b.trading_end))
```

**What this does**: Sort all banks (including the split ones) by start time. If two banks start at the same time, sort by end time.

`lambda b: (b.trading_start, b.trading_end)` is just a shortcut for "sort by start first, then by end as a tiebreaker."

Example:
```
Before sorting: [RBS 9-16], [Tokyo 0-6], [Tokyo 22-24], [MS 11-17]
After sorting:  [Tokyo 0-6], [RBS 9-16], [MS 11-17], [Tokyo 22-24]
```

---

### Step 3: Handle Midnight-Wrapping Orders

```python
    if order.end_time < order.start_time:
        order1 = Order(0, order.end_time)
        order2 = Order(order.start_time, 24)
        return (can_trade_monotonic_4(order1, expanded) and
                can_trade_monotonic_4(order2, expanded))
```

**What this does**: If the ORDER wraps past midnight, split it into two halves. BOTH halves must be covered.

Example:
- Order: 23:00–3:00 → `end_time (3) < start_time (23)` → wraps!
- Split into: order1 = [0–3] and order2 = [23–24]
- Check: Can banks cover [0–3]? AND can banks cover [23–24]?
- Both must be True for the trade to succeed.

---

### Step 4: Normal Orders

```python
    return can_trade_monotonic_4(order, expanded)
```

**What this does**: If the order doesn't wrap midnight, just run the normal sweep check directly.

---

## Complete Example with Midnight Wrapping

```python
banks = [
    Bank("RBS", 9, 16),
    Bank("Tokyo", 22, 6),   # Wraps midnight!
]

order = Order(23, 3)  # Also wraps midnight!
```

**Step 1 — Split wrapping banks:**
```
Tokyo [22-6] → Tokyo [0-6] + Tokyo [22-24]
Result: [RBS 9-16], [Tokyo 0-6], [Tokyo 22-24]
```

**Step 2 — Sort:**
```
[Tokyo 0-6], [RBS 9-16], [Tokyo 22-24]
```

**Step 3 — Split wrapping order:**
```
Order [23-3] → order1 [0-3] + order2 [23-24]
```

**Check order1 [0-3]:**
```
current_start = 0
Bank [Tokyo 0-6]: 0 < 0? No. 3 ≤ 6? YES → True ✅
```

**Check order2 [23-24]:**
```
current_start = 23
Bank [Tokyo 0-6]: 23 < 0? No. 24 ≤ 6? No. 23 < 6? No. Skip.
Bank [RBS 9-16]: 23 < 9? No. 24 ≤ 16? No. 23 < 16? No. Skip.
Bank [Tokyo 22-24]: 23 < 22? No. 24 ≤ 24? YES → True ✅
```

**Both True → can_trade_4 returns True ✅**

---

## Summary

| Function | Job |
|---|---|
| `can_trade_monotonic_4` | The engine — does the sorted sweep assuming no midnight wrapping |
| `can_trade_4` | The orchestrator — splits wrapping banks/orders, sorts, then calls the engine |

The key insight: **midnight wrapping is hard to handle in one pass, so we eliminate it first by splitting, then use the simple sweep.**
