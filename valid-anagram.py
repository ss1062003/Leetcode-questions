# Problem Statement:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Approach 1: Using Collection Counter
# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)

# # Example usage:
# sol = Solution()
# print(sol.isAnagram("anagram", "nagaram"))  # Output: True
# print(sol.isAnagram("rat", "car"))          # Output: False

# Approach 2:
# Using a dictionary to count character frequencies
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # Early exit if lengths differ
#         if len(s) != len(t):
#             return False

#         # Count character frequency for both strings
#         count_s = {}
#         count_t = {}

#         for char in s:
#             count_s[char] = count_s.get(char, 0) + 1

#         for char in t:
#             count_t[char] = count_t.get(char, 0) + 1

#         # Compare the two dictionaries
#         return count_s == count_t

# Example usage
# solution = Solution()
# str1 = "listen"
# str2 = "silent"

# if solution.isAnagram(str1, str2):
#     print(f'"{str1}" and "{str2}" are anagrams.')
# else:
#     print(f'"{str1}" and "{str2}" are not anagrams.')

#Approach 3: Using Sorting
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # Early exit if lengths differ
#         if len(s) != len(t):
#             return False
#         # Sort both strings and compare
#         return sorted(s) == sorted(t)
# Example usage
# solution = Solution()
# str1 = "listen"
# str2 = "silent"
# if solution.isAnagram(str1, str2):
#     print(f'"{str1}" and "{str2}" are anagrams.')
# else:
#     print(f'"{str1}" and "{str2}" are not anagrams.')

# Approach 4: Using a single dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if lengths differ
        if len(s) != len(t):
            return False

        # Count character frequency using a single dictionary
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1
            if count[char] < 0:
                return False

        # All counts should be zero
        return all(value == 0 for value in count.values())

# ✅ Example usage (outside the class)
solution = Solution()
str1 = "listen"
str2 = "silent"

if solution.isAnagram(str1, str2):
    print(f'"{str1}" and "{str2}" are anagrams.')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')
    

