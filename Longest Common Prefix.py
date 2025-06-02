class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        prefix = strs[0]

        # Compare with each string
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Shorten the prefix
                if not prefix:
                    return ""

        return prefix

