# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def canEatAll(speed: int) -> bool:
            return sum((pile + speed - 1) // speed for pile in piles) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canEatAll(mid):
                right = mid
            else:
                left = mid + 1

        return left
# Example usage:
solution = Solution()
print(solution.minEatingSpeed([3, 6, 7, 11], 8))  # Output: 4
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Output: 30
print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))  # Output: 23
print(solution.minEatingSpeed([312884470], 312884469))  # Output: 2