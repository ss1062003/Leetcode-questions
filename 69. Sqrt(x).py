#69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

#1. Brute Force Approach
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         i = 0
#         while i * i <= x:
#             i += 1
#         return i - 1
# Example usage:
# solution = Solution() 
# print(solution.mySqrt(4))  # Output: 2
# print(solution.mySqrt(8))  # Output: 2

#2. Binary Search Approach
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 2:
#             return x
        
#         left, right = 2, x // 2
#         while left <= right:
#             mid = (left + right) // 2
#             square = mid * mid
            
#             if square == x:
#                 return mid
#             elif square < x:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return right
# Example usage:
# solution = Solution()
# print(solution.mySqrt(4))  # Output: 2
# print(solution.mySqrt(8))  # Output: 2   

#3. Newton's Method Approach
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 2:
#             return x
        
#         guess = x // 2
#         while guess * guess > x:
#             guess = (guess + x // guess) // 2
        
#         return guess
# Example usage:
# solution = Solution()
# print(solution.mySqrt(4))  # Output: 2
# print(solution.mySqrt(8))  # Output: 2

#4. Bit Manipulation Approach
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        result = 0
        bit = 1 << 30  # Start with the highest bit that can be set for 32-bit integers
        
        while bit > 0:
            temp = result | bit
            if temp * temp <= x:
                result = temp
            bit >>= 1
        
        return result

# Example usage:
solution = Solution()
print(solution.mySqrt(4))  # Output: 2
print(solution.mySqrt(16))  # Output: 4

