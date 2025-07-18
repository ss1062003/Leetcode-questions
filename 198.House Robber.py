# 198. House Robber
# https://leetcode.com/problems/house-robber/

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount
# of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.




class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0  # rob1: dp[i-2], rob2: dp[i-1]
        for num in nums:
            newRob = max(rob2, rob1 + num)
            rob1 = rob2
            rob2 = newRob
        return rob2
# Example usage:
solution = Solution()
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12
print(solution.rob([2, 1, 1, 2]))  # Output: 4
print(solution.rob([5, 3, 4, 11, 2]))  # Output: 16

