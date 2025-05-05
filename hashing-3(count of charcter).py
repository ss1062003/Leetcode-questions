# 🎯 Problem Statement
# Given an array of integers, count how many times each unique element appears.
# ✅ Example
# arr = [1, 2, 2, 3, 3, 3]
# Expected output:
# {1: 1, 2: 2, 3: 3}

def freq_count(arr):
    freq = {}  # initialize empty dictionary
    for item in arr:
        if item in freq:
            freq[item] += 1  # if already exists, increment count
        else:
            freq[item] = 1   # if not, initialize count to 1
    return freq

arr = [1,2,2,2,3,4,5,7,2,3,4,1,4,1,3,3,3,3]
print(freq_count(arr))  # Output: {1: 3, 2: 4, 3: 6, 4: 3, 5: 1, 7: 1}

# | Aspect         | Value                                |
# | -------------- | ------------------------------------ |
# | Time           | **O(n)** — Single pass through array |
# | Space          | **O(n)** — To store frequencies      |
# | Technique      | Hashing                              |
# | Data Structure | Python `dict` (hash map)             |

