class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        res = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                res.append(path)
                return
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return res

# Example usage:
solution = Solution()
print(solution.letterCombinations("23"))  # Output: ["ad", "ae",
# "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(solution.letterCombinations(""))  # Output: []
print(solution.letterCombinations("2"))  # Output: ["a", "b", "c"]
        