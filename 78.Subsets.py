# 78. Subsets.py
# Given a set of distinct integers, nums, return all possible subsets (the power set).
# The solution uses backtracking to generate all subsets of the input list nums.
# The function subsets() generates all subsets of the input list nums.
# The function backtrack() generates all subsets of the input list nums using backtracking.
# The function main() tests the function subsets() with a sample input list nums.

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(start: int, path: List[int]):
            result.append(path[:])  # Append a copy of the current path

            for i in range(start, n):
                path.append(nums[i])  # Include nums[i]
                backtrack(i + 1, path)  # Move to the next index
                path.pop()  # Backtrack

        backtrack(0, [])
        return result
# Example usage:
solution = Solution()
print(solution.subsets([1, 2, 3]))  # Output: [[],
# [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
print(solution.subsets([0]))  # Output: [[], [0]]
print(solution.subsets([1, 2]))  # Output: [[], [1], [2], [1, 2]]
# Time complexity: O(2^n) 
# Space complexity: O(n) 
# Note: The result includes all subsets, including the empty set and the full set.
# The subsets function generates all possible subsets of the input list nums using backtracking.
# It starts with an empty path and explores all combinations by either including or excluding each element.
