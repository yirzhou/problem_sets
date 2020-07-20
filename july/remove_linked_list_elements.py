# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """#203. Remove all elements from a linked list of integers that have value val."""
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val: head = head.next
        curr = head
        while curr is not None and curr.next is not None:
            if curr.next.val == val: curr.next = curr.next.next
            else: curr = curr.next
        return head
