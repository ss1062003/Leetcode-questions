#  Problem Statement (LeetCode #1: Two Sum)
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



def twoSum(nums, target):
    hashmap = {}  # Stores number -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i


# 🔸 Example

# Input: nums = [2, 7, 11, 15], target = 9  
# Output: [0, 1]
# Because nums[0] + nums[1] == 2 + 7 == 9

#Optimal Solution (Using HashMap - O(n) time complexity)

def twoSum(nums, target):
    hashmap = {}  # Stores number -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i


# 🧠 How It Works:
# You iterate through each number.

# Calculate the difference between the target and current number.

# If that difference is already in the hashmap, you found the pair.

# Otherwise, add the current number and its index to the hashmap
