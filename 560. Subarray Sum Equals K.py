#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        sum_freq = {0: 1}  # prefix_sum: frequency

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in sum_freq:
                count += sum_freq[prefix_sum - k]

            sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

        return count
# Example usage:
solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))  # Output: 2
print(solution.subarraySum([1, 2, 3], 3))  # Output: 2
print(solution.subarraySum([1, -1, 0], 0))  # Output: 3
