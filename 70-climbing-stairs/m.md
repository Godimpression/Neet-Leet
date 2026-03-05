# LeetCode 70: Climbing Stairs

You are climbing a staircase that takes `n` steps to reach the top. Each time you can either climb **1** or **2** steps. This algorithm calculates the number of distinct ways to reach the top.

---

## ### Logic Examples: Climbing Stairs Algorithm

The algorithm uses **Dynamic Programming** to solve for `n` by looking at the two previous steps.

#### 1. Case: $n=2$
- **Input:** `n = 2`
- **Step 1:** 1 step + 1 step
- **Step 2:** 2 steps
- **Result:** Returns `2`

#### 2. Case: $n=3$
- **Input:** `n = 3`
- **Option 1:** 1+1+1
- **Option 2:** 1+2
- **Option 3:** 2+1
- **Result:** Returns `3`



---

## ### Complexity Analysis

| Approach | Time Complexity | Space Complexity | Result |
| :--- | :--- | :--- | :--- |
| **Brute Force** | $O(2^n)$ | $O(n)$ | **Time Limit Exceeded** |
| **Memoization** | $O(n)$ | $O(n)$ | **Accepted (0ms / 100%)** |
| **Iterative** | $O(n)$ | $O(1)$ | **Best Space Efficiency** |

---

## ### Final Optimized Solution (Top-Down)

This solution uses a **Memoization Table** (dictionary) defined at the class level to ensure the data persists across recursive calls, preventing redundant work.

```python
class Solution:
    # Memoization table defined at class level to persist across calls
    memo = {} 

    def climbStairs(self, n: int) -> int:
        # 1. Check if result is already in the "cheat sheet"
        if n in self.memo:
            return self.memo[n]
        
        # 2. Base Cases
        if n == 1: return 1
        if n == 2: return 2
        
        # 3. Recursive step: store result in memo before returning
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]

### Option 2: Iterative Solution (The Loop)This is the most efficient version for memory. Instead of recursion, it uses a simple loop to calculate the next step based on the last two.Pythonclass Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n # Base cases
            
        # We only track the two previous steps
        prev2, prev1 = 1, 2 
        
        for i in range(3, n + 1):
            current = prev1 + prev2 # The Fibonacci logic
            prev2 = prev1 # Shift pointers forward
            prev1 = current
            
        return prev1
### Step-by-Step Trace for $n=5$Initial: prev2 = 1, prev1 = 2Step 3: $1 + 2 = \mathbf{3}$Step 4: $2 + 3 = \mathbf{5}$Step 5: $3 + 5 = \mathbf{8}$End: The function returns 8.
