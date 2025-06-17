#  55. Jump Game
# Difficulty: Medium
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
        return True
# Example usage:
solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))
# Output: True
print(solution.canJump([3, 2, 1, 0, 4]))    
# Output: False
print(solution.canJump([0]))  # Output: True
print(solution.canJump([2, 0, 0]))  # Output: True
print(solution.canJump([1, 0, 0, 0]))  # Output: True
