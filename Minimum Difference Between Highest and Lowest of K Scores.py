# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

 

# Example 1:

# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.
# Example 2:

# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.
 

# Constraints:

# 1 <= k <= nums.length <= 1000
# 0 <= nums[i] <= 105


from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 0 or len(nums) < k:
            return 0  # edge case: no comparison needed

        nums.sort() #Because in a sorted array, the minimum difference between any group of k numbers will be found in a contiguous subarray
        min_diff = float('inf')

        for i in range(len(nums) - k + 1):
            current_diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, current_diff)

# nums = [70, 80, 85, 90, 100], k = 3
# i = 0 → [70, 80, 85] → diff = 85 - 70 = 15

# i = 1 → [80, 85, 90] → diff = 90 - 80 = 10 

# i = 2 → [85, 90, 100] → diff = 100 - 85 = 15

# Minimum difference = 10

        return min_diff
    
#  Time Complexity
# Sorting: O(n log n)

# Window loop: O(n)

# → Total: O(n log n)

#  Space Complexity
# O(1) (in-place sorting and constant extra space)
