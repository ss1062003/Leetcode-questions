# add Two Numbers(Singly Linked List)(Medium)
# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and carry == 0:
            return None

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry

        node = ListNode(total % 10)
        node.next = self.addTwoNumbers(
            l1.next if l1 else None,
            l2.next if l2 else None,
            total // 10
        )
        return node
# Example usage:
# Assuming ListNode is defined as follows:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
while result:
    print(result.val, end=' ')
    result = result.next


