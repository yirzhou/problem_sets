class ListNode(object):
    def __init__(self, x):
        self.val, self.next = x, None

class Solution:
    def __init__(self): return

    def middle_node(self, head):
        '''Main idea is to have two pointers: slow and fast.
        - The fast will traverse the list at 2X speed.
        - The middle is found when fast is at the end.
        '''
        if not head.next: return head

        fast, slow = head, head
        while fast:
            try: fast = fast.next.next
            except Exception: return slow
            slow = slow.next
        return slow

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)

    print(Solution().middle_node(head).val)

if __name__ == '__main__': main()
