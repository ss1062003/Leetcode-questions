# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes
        current.next = list1 if list1 else list2
        
        return dummy.next

# Example usage:
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
# Creating two sorted linked lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
# Merging the two lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
# Printing the merged list
print_list(merged_list)
