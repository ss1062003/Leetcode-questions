#56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # Step 1: Sort the intervals by start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # Overlap condition
                last[1] = max(last[1], current[1])  # Merge intervals
            else:
                merged.append(current)

        return merged

# Example usage:
solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
print(solution.merge([[1, 4], [4, 5]]))  # Output
# Output: [[1, 5]]
# Time complexity: O(n log n) due to sorting
# Space complexity: O(n) for the merged list
# Note: The input intervals are assumed to be non-empty and well-formed.

print(solution.merge([[1, 4], [2, 3], [5, 7], [6, 8]]))  # Output: [[1, 4], [5, 8]]