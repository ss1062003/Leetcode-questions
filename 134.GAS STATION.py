# 134. Gas Station
# https://leetcode.com/problems/gas-station/
# Time: O(n)
# Space: O(1)
# 134. Gas Station
# You are given two integer arrays gas and cost. gas[i] represents the amount of gas
# of the ith gas station, and cost[i] represents the amount of gas required to travel from the ith gas station to the next (i + 1)th gas station. You can start at any gas station.
# Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique.

# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3

# Example 2:
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1

# Example 3:
# Input: gas = [5,1,2,3,4], cost = [4,4,1,5,1]
# Output: 3



class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas = total_cost = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_gas >= total_cost else -1

# Example usage:
solution = Solution()
print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # Output: 3
print(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # Output: -1
print(solution.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))  # Output: 3
print(solution.canCompleteCircuit([1, 2, 3], [2, 3, 4]))  # Output: -1
print(solution.canCompleteCircuit([3, 1, 2], [2, 2, 3]))  # Output: 0
