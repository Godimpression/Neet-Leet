# 70. Climbing Stairs

### 💡 Intuition
To reach the $n^{th}$ step, you must have come from either the $(n-1)^{th}$ step (by taking 1 step) or the $(n-2)^{th}$ step (by taking 2 steps). Therefore, the total number of ways to reach step $n$ is simply the sum of the ways to reach the two previous steps: $f(n) = f(n-1) + f(n-2)$. This mirrors the Fibonacci sequence pattern.

---

### 🚀 Approach

#### Option 1: Top-Down Recursion (Memoization)
To avoid the **Time Limit Exceeded** error caused by redundant calculations, we use a dictionary (`memo`) to store the result of each step the first time it is calculated.
- **Check Memo:** Before calculating, check if `n` exists in the dictionary.
- **Base Cases:** If $n=1$ return 1; if $n=2$ return 2.
- **Store & Return:** Save the sum of the two previous recursive calls in the memo.



#### Option 2: Bottom-Up Iteration (The Loop)
This is the most space-efficient method. Instead of recursion, we use a loop to "climb" from step 3 up to $n$, only keeping track of the last two values.
- **Initialize:** Start with `prev2 = 1` and `prev1 = 2`.
- **Loop:** For each step from 3 to $n$, calculate the `current` sum and shift the pointers forward.



---

### 📊 Complexity

#### **Memoization Approach**
* **Time complexity:** $O(n)$ — Each step from 1 to $n$ is computed exactly once.
* **Space complexity:** $O(n)$ — Required for the recursion stack and the dictionary storage.

#### **Iterative Loop Approach**
* **Time complexity:** $O(n)$ — A single pass through the loop from 3 to $n$.
* **Space complexity:** $O(1)$ — Only two variables are stored regardless of the size of $n$.

------------------------------------------------------------------------------------------------------
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
