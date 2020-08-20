# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None: return
        slow, fast = head, head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        tmp = slow.next
        slow.next = None
        
        new_head = self.reverse_list(tmp)
        cur = head
        while cur is not None and new_head is not None:
            tmp1, tmp2 = cur.next, new_head.next
            cur.next = new_head
            new_head.next = tmp1
            cur = tmp1
            new_head = tmp2
        
        
    def reverse_list(self, head):
        if head is None or head.next is None: return head
        node = head.next
        head.next = None
        while node is not None:
            tmp = node.next
            node.next = head
            head = node
            node = tmp
        return head
        