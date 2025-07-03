#3304. Find the K-th Character in String Game 
# https://leetcode.cn/problems/find-the-k-th-character-in-string-game-i/

# Alice and Bob are playing a game. Initially, Alice has a string word = "a".

# You are given a positive integer k.

# Now Bob will ask Alice to perform the following operation forever:

# Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
# For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

# Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

# Note that the character 'z' can be changed to 'a' in the operation.

# Example 1:
# Input: k = 5
# Output: "b"

# Explanation:
# Initially, word = "a". We need to do the operation three times:
# Generated string is "b", word becomes "ab".
# Generated string is "bc", word becomes "abbc".
# Generated string is "bccd", word becomes "abbcbccd".

# Example 2:
# Input: k = 10
# Output: "c"

#METHOD 1: Iterative Approach
# Time Complexity: O(k)
# class Solution:
#     def kthCharacter(self, k: int) -> str:
#         word = "a"
        
#         while len(word) < k:
#             next_part = ''.join(
#                 chr(((ord(c) - ord('a') + 1) % 26) + ord('a')) for c in word
#             )
#             word += next_part
        
#         return word[k - 1]

# # Example usage:
# solution = Solution()
# print(solution.kthCharacter(5))  # Output: "b"
# print(solution.kthCharacter(10)) # Output: "c"
# print(solution.kthCharacter(1))  # Output: "a"

#METHOD 2: Mathematical Approach
# Time Complexity: O(log k)
#THIS METHOD IS NOT CORRECT, IT WILL GIVE WRONG OUTPUT FOR SOME TEST CASES
# # The string does not repeat every 26 characters. It keeps growing exponentiallY
# class Solution:
#     def kthCharacter(self, k: int) -> str:
#         # Calculate the number of complete cycles of 26 characters
#         cycle_length = 26
#         cycle_count = (k - 1) // cycle_length
        
#         # Calculate the index within the current cycle
#         index_in_cycle = (k - 1) % cycle_length
        
#         # The character is determined by the initial character 'a' plus the index in the cycle
#         return chr(ord('a') + index_in_cycle)
# # Example usage:
# solution = Solution()
# print(solution.kthCharacter(5))  # Output: "b"
# print(solution.kthCharacter(10)) # Output: "c"

#METHOD 3: Recursive Approach
# Time Complexity: O(log k)
class Solution:
    def kthCharacter(self, k: int) -> str:
        def get_char(k):
            if k == 1:
                return 'a'
            length = 1
            while length * 2 < k:
                length *= 2
            if k <= length:
                return get_char(k)
            else:
                original = get_char(k - length)
                return chr(((ord(original) - ord('a') + 1) % 26) + ord('a'))

        return get_char(k)
# Example usage:
solution = Solution()
print(solution.kthCharacter(5))  # Output: "b"
print(solution.kthCharacter(10)) # Output: "c"