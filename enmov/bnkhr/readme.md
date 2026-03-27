# BankHours: Method Comparison & Analysis

## The Problem
Given a list of bank operating hours (e.g., `["09:00-16:00", "11:00-17:00"]`), determine if a requested trade time falls within the valid range.

---

## Your Method (Loop Every Time)

```python
class bankhours:
    def __init__(self, selected_hours):
        self.dict = set(selected_hours)

    def trade(self, trade_hours):
        starting = []
        ending = []

        for i in self.dict:
            start = i[0:2]
            end = i[6:8]
            starting.append(start)
            ending.append(end)

        min_start = min(starting)
        max_ending = max(ending)

        if trade_hours[0:2] >= min_start and trade_hours[6:8] <= max_ending:
            return "Success"
        return "Failure"
```

### How it works:
- `__init__` just stores the hours in a set — no processing.
- Every time `trade()` is called, it:
  1. Loops through ALL hours in the set
  2. Builds two lists (`starting` and `ending`)
  3. Finds `min()` and `max()` from those lists
  4. Then checks the trade time

### Issues:
- **Repeated work**: If you call `trade()` 1000 times, it loops through the dictionary 1000 times.
- **String comparison**: Comparing `"08"` vs `"09"` works only if hours are zero-padded. `"9"` > `"17"` is `True` in string comparison, which is WRONG.
- **Extra space**: Creates two new lists every single call.

---

## My Method (Precompute in `__init__`)

```python
class BankHours:
    def __init__(self, selected_hours):
        self.min_open = 24
        self.max_close = 0

        for h in selected_hours:
            open_hr, close_hr = h.split("-")
            open_val = int(open_hr.split(":")[0])
            close_val = int(close_hr.split(":")[0])
            self.min_open = min(self.min_open, open_val) 
            self.max_close = max(self.max_close, close_val)
            # for every loop, max and min is calculated and stored in to min_open and max_open  and then to be compared with the next open_val,close val. SO no need of o(n) lists. this is o(1)

    def trade(self, trade_hours):
        open_hr, close_hr = trade_hours.split("-")
        trade_open = int(open_hr.split(":")[0])
        trade_close = int(close_hr.split(":")[0])

        if trade_open >= self.min_open and trade_close <= self.max_close:
            return "Success"
        return "Failure"
```

### How it works:
- `__init__` does the heavy lifting ONCE:
  1. Loops through all hours
  2. Calculates `min_open` and `max_close`
  3. Stores them as integers on `self`
- `trade()` just compares two numbers — no loops, no lists, instant.

### Why it's better:
- **No repeated work**: min/max are calculated once, reused forever.
- **Integer comparison**: `9 > 17` is correctly `False`. No zero-padding issues.
- **No extra space**: No lists created. Just two integers stored.

---

## The Key Difference: Where the Work Happens

### Your Method
```
__init__  →  Does almost nothing (just stores data)
trade()   →  Does ALL the work every single time
```

### My Method
```
__init__  →  Does ALL the work once upfront
trade()   →  Does almost nothing (just compares two numbers)
```

Think of it this way:
- **Your method** = A restaurant that goes grocery shopping every time a customer orders.
- **My method** = A restaurant that stocks the kitchen once, then cooks instantly when orders come in.

---

## Time & Space Complexity Comparison

Let N = number of time ranges in the dictionary.
Let Q = number of times `trade()` is called.

### Your Method

| Operation | Time | Space | Why |
|-----------|------|-------|-----|
| `__init__` | O(N) | O(N) | Stores N items in a set |
| `trade()` (single call) | O(N) | O(N) | Loops through all N items, builds 2 lists of size N |
| `trade()` (Q calls) | **O(N × Q)** | O(N) | Repeats the full loop Q times |

### My Method

| Operation | Time | Space | Why |
|-----------|------|-------|-----|
| `__init__` | O(N) | O(1) | Loops once, stores only 2 integers |
| `trade()` (single call) | **O(1)** | **O(1)** | Just compares 2 integers |
| `trade()` (Q calls) | **O(Q)** | **O(1)** | Each call is O(1), so Q calls = O(Q) |

### Total Complexity (init + Q trade calls)

| | Your Method | My Method |
|---|---|---|
| **Time** | O(N) + O(N × Q) = **O(N × Q)** | O(N) + O(Q) = **O(N + Q)** |
| **Space** | **O(N)** | **O(1)** extra space |

### Real-World Example

If you have 1,000 bank hour ranges and call `trade()` 10,000 times:

| | Your Method | My Method |
|---|---|---|
| **Operations** | 1,000 × 10,000 = **10,000,000** | 1,000 + 10,000 = **11,000** |
| **Speedup** | — | **~909x faster** |

---

## Usage

```python
# Create the bank (calls __init__ once)
chase = BankHours(["09:00-16:00", "11:00-17:00"])

# Call trade as many times as needed (each call is O(1))
print(chase.trade("10:00-16:00"))   # Success
print(chase.trade("08:00-17:00"))   # Failure
print(chase.trade("09:00-15:00"))   # Success
print(chase.trade("07:00-12:00"))   # Failure
```

---

## Summary

The interview insight: **Do the heavy work once in `__init__`, so repeated queries via `trade()` are instant.** This is a common pattern in system design — precompute what you can.
