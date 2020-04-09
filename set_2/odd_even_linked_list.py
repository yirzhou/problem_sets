class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self): return

    def odd_even_list(self, head):
        '''Group odd and even nodes together in-place in O(N) time and O(1) space.
        '''
        odd_head, even_head = head, head.next
        odd_node, even_node = odd_head, even_head

        while True:
            if not even_node: break
            odd_node.next = even_node.next
            if not odd_node.next: break
            odd_node = odd_node.next
            even_node.next = odd_node.next
            even_node = even_node.next

        odd_node.next = even_head
        return head

    def print_list(self, list_node):
        head = list_node
        arr = []
        while(head):
            arr.append(head.val)
            head = head.next

        return arr

def main():
    head = ListNode(2)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(6)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(7)
    
    solution = Solution()
    list_head = solution.odd_even_list(head)
    print(solution.print_list(list_head))

if __name__ == '__main__': main()