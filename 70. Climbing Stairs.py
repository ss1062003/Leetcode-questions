## 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second
# Example usage:
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(4))  # Output: 5
print(solution.climbStairs(5))  # Output: 8