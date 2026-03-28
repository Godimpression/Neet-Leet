# canTrade: 5 Solutions Explained (Python)

## The Problem

You have a list of **banks**, each with trading hours (e.g., RBS: 9:00–16:00). You receive an **order** with a start and end time. **Can the order be fully covered by the combined trading hours of all banks?**

Example banks:
- RBS: 9–16
- Morgan Stanley: 11–17
- JP Morgan: 14–20
- NAB: 2–7

Together RBS + MS + JPM cover **9:00–20:00** continuously. So an order from 10–17 is valid, but 15–21 is not (gap after 20).

---

## Data Structures

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

---

## Solution 1: Brute Force (Keep Scanning Until Stuck)

**Idea**: Stand at the order's start time. Ask every bank "can you carry me forward?" If yes, jump to that bank's end. Repeat until you reach the order's end or get stuck.

**Why multiple passes?** Banks are unsorted. A bank later in the list might cover a gap that an earlier one couldn't.

```python
def can_trade_1(order, banks):
    current_start = order.start_time
    matched = True

    while matched:
        matched = False
        for bank in banks:
            if bank.trading_start <= current_start < bank.trading_end:
                current_start = bank.trading_end
                if order.end_time <= current_start:
                    return True
                matched = True

    return False
```

| | Value |
|---|---|
| **Time** | O(N²) — up to N passes, each scanning N banks |
| **Space** | O(1) — no extra data structures |

✅ Simple logic, no preprocessing needed
❌ Slowest solution — repeated full scans

---

## Solution 2: Merge Banks First, Then Check

**Idea**: Before checking any order, merge all overlapping banks into a clean sorted timeline. Then just check if the order fits inside one merged range.

```
Before: [9-16] [11-17] [14-20] [2-7]
After:  [2-7] [9-20]
```

```python
def merge_bank(merged, bank_start, bank_end, bank_name):
    """Insert or merge a bank into the sorted non-overlapping merged list."""
    for i, m in enumerate(merged):
        if m["start"] <= bank_end and bank_start <= m["end"]:
            # Overlaps — extend the existing range
            m["start"] = min(m["start"], bank_start)
            m["end"] = max(m["end"], bank_end)
            m["name"] += " + " + bank_name
            return
        elif bank_end < m["start"]:
            # Insert before this one (no overlap possible after)
            merged.insert(i, {"name": bank_name, "start": bank_start, "end": bank_end})
            return
    merged.append({"name": bank_name, "start": bank_start, "end": bank_end})


def merge_banks(banks):
    """Merge all banks into a sorted non-overlapping list. Handles midnight wrapping."""
    merged = []
    for bank in banks:
        if bank.trading_end < bank.trading_start:
            # Wraps past midnight — split into two
            merge_bank(merged, 0, bank.trading_end, bank.name)
            merge_bank(merged, bank.trading_start, 24, bank.name)
        else:
            merge_bank(merged, bank.trading_start, bank.trading_end, bank.name)
    return merged


def can_trade_monotonic_2(order, merged):
    """Check if order fits inside one merged range."""
    for m in merged:
        if order.start_time < m["start"]:
            return False
        if order.end_time <= m["end"]:
            return True
    return False


def can_trade_2(order, banks):
    merged = merge_banks(banks)

    if order.end_time < order.start_time:
        # Order wraps midnight — check both halves
        half1 = Order(order.start_time, 24)
        half2 = Order(0, order.end_time)
        return can_trade_monotonic_2(half1, merged) and can_trade_monotonic_2(half2, merged)

    return can_trade_monotonic_2(order, merged)
```

| | Value |
|---|---|
| **Time** | O(N²) for merging, O(N) for checking |
| **Space** | O(N) — new merged list |

✅ Handles midnight wrapping correctly
✅ After merging, the check is very fast
❌ Most complex code of all 5 solutions

---

## Solution 3: Sort, Then Sweep (The Interview Answer)

**Idea**: Sort banks by start time. Then one single pass with a pointer — if there's a gap, you know immediately.

Walk left to right:
1. If `current_start` is before this bank starts → **gap!** → fail
2. If this bank covers the order's end → **done!** → success
3. Otherwise push `current_start` to this bank's end

```python
def can_trade_3(order, banks):
    # Sort banks by trading start time
    sorted_banks = sorted(banks, key=lambda b: b.trading_start)

    current_start = order.start_time

    for bank in sorted_banks:
        if current_start < bank.trading_start:
            # Gap found — no bank covers this time
            return False
        if order.end_time <= bank.trading_end:
            # This bank covers the rest of the order
            return True
        if current_start < bank.trading_end:
            # Push forward to this bank's end
            current_start = bank.trading_end

    return False
```

**Example walkthrough** — order 10–17, sorted banks: [2–7], [9–16], [11–17], [14–20]:
- current_start = 10
- [2–7]: doesn't help (ends at 7)
- [9–16]: covers 10, push current_start → 16
- [11–17]: 17 ≤ 17 → **success!** ✅

| | Value |
|---|---|
| **Time** | O(N log N) for sort + O(N) sweep = **O(N log N)** |
| **Space** | O(N) for the sorted copy |

✅ Clean, elegant, great for interviews
✅ Single pass after sorting
❌ Doesn't handle midnight wrapping

---

## Solution 4: Sort + Sweep + Midnight Wrapping

**Idea**: Same as Solution 3, but first split any bank or order that wraps past midnight.

- Tokyo (22:00–6:00) → split into [0–6] and [22–24]
- Order 23:00–3:00 → split into [23–24] AND [0–3], both must pass

```python
def can_trade_monotonic_4(order, sorted_banks):
    """Same sweep as Solution 3."""
    current_start = order.start_time

    for bank in sorted_banks:
        if current_start < bank.trading_start:
            return False
        if order.end_time <= bank.trading_end:
            return True
        if current_start < bank.trading_end:
            current_start = bank.trading_end

    return False


def can_trade_4(order, banks):
    # Split any midnight-wrapping banks into two
    expanded = []
    for bank in banks:
        if bank.trading_end < bank.trading_start:
            expanded.append(Bank(bank.name, 0, bank.trading_end))
            expanded.append(Bank(bank.name, bank.trading_start, 24))
        else:
            expanded.append(bank)

    # Sort by start time, then end time
    expanded.sort(key=lambda b: (b.trading_start, b.trading_end))

    # Split midnight-wrapping orders into two checks
    if order.end_time < order.start_time:
        order1 = Order(0, order.end_time)
        order2 = Order(order.start_time, 24)
        return (can_trade_monotonic_4(order1, expanded) and
                can_trade_monotonic_4(order2, expanded))

    return can_trade_monotonic_4(order, expanded)
```

| | Value |
|---|---|
| **Time** | O(N log N) — same as Solution 3 |
| **Space** | O(N) — extra banks from splitting |

✅ Handles midnight wrapping correctly
✅ Same efficient sweep as Solution 3
❌ Slightly more complex

---

## Solution 5: Boolean Hour Array (The Visual One)

**Idea**: Create a 24-slot timeline. Paint every bank's hours as `True`. Then check if every hour of the order is `True`.

```
Hour:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
NAB:         [T  T  T  T  T]
RBS:                           [T  T  T  T  T  T  T]
MS:                                 [T  T  T  T  T  T  T]
JPM:                                          [T  T  T  T  T  T  T]

Order 10-17: All True? → YES ✅
Order 15-21: Hour 21 = False → NO ❌
```

```python
def can_trade_5(order, banks):
    is_open = [False] * 24

    for bank in banks:
        for h in range(bank.trading_start, bank.trading_end + 1):
            is_open[h] = True

    for h in range(order.start_time, order.end_time + 1):
        if not is_open[h]:
            return False

    return True
```

| | Value |
|---|---|
| **Time** | O(N × 24) = **O(N)** since 24 is a constant |
| **Space** | O(24) = **O(1)** — fixed-size array |

✅ Simplest and most intuitive
✅ Fastest in terms of big-O
✅ Easy to visualize and debug
❌ Only works because hours are whole numbers 0–23
❌ Doesn't handle midnight wrapping

---

## Test It All

```python
banks = [
    Bank("Royal Bank of Scotland", 9, 16),
    Bank("Morgan Stanley", 11, 17),
    Bank("JP Morgan", 14, 20),
    Bank("National Australia Bank", 2, 7),
]

test_cases = [
    (Order(10, 17), True),   # 10:00–17:00 → covered by RBS+MS
    (Order(15, 21), False),  # 15:00–21:00 → gap after 20:00
    (Order(4, 10),  False),  # 04:00–10:00 → gap 7:00–9:00
]

for order, expected in test_cases:
    print(f"Order({order.start_time}-{order.end_time}): expected={expected}")
    print(f"  Solution 1: {can_trade_1(order, banks)}")
    print(f"  Solution 2: {can_trade_2(order, banks)}")
    print(f"  Solution 3: {can_trade_3(order, banks)}")
    print(f"  Solution 4: {can_trade_4(order, banks)}")
    print(f"  Solution 5: {can_trade_5(order, banks)}")
    print()
```

---

## Side-by-Side Comparison

| | Solution 1 | Solution 2 | Solution 3 | Solution 4 | Solution 5 |
|---|---|---|---|---|---|
| **Approach** | Brute force loop | Merge then check | Sort then sweep | Sort + sweep + midnight | Boolean array |
| **Time** | O(N²) | O(N²) | O(N log N) | O(N log N) | O(N) |
| **Space** | O(1) | O(N) | O(N) | O(N) | O(1) |
| **Midnight wrap** | ❌ | ✅ | ❌ | ✅ | ❌ |
| **Code complexity** | Simple | Complex | Clean | Medium | Simplest |

---

## When to Use Which?

| Scenario | Use |
|---|---|
| **Learning** | Solution 5 — visual, obvious |
| **Interview** | Solution 3 — clean, shows algorithmic thinking |
| **Interview + edge cases** | Solution 4 — shows you handle midnight |
| **Production** | Solution 2 or 4 — handles everything |
| **Quick prototype** | Solution 1 — no setup needed |

---

## Key Takeaway

All 5 solutions answer the same question: **"Is there a continuous chain of bank coverage from order start to order end?"**

1. **Solution 1**: Keep scanning until nothing moves (brute force)
2. **Solution 2**: Merge everything first, then one clean check (preprocess)
3. **Solution 3**: Sort first, then one clean sweep (sort + greedy)
4. **Solution 4**: Solution 3 but handles midnight (sort + greedy + edge cases)
5. **Solution 5**: Paint the hours on a timeline and check (bitmap)
