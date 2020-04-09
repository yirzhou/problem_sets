import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self): return

    def merge_k_lists(self, lists):
        heap = []

        merged_list = ListNode(None)
        list_head = merged_list

        # push all of the minimum items onto the heap
        for i in range(len(lists)): 
            head = lists[i]
            heapq.heappush(heap, (head.val, i))

        while len(heap):
            val, index = heapq.heappop(heap)
            list_head.next = ListNode(val)
            list_head = list_head.next
            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(heap, (lists[index].val, index))
        merged_list = merged_list.next
        return merged_list

    def print_list(self, list_node):
        head = list_node
        arr = []
        while(head.next):
            arr.append(head.val)
            head = head.next

        return arr

    
def main():
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    solution = Solution()
    merged_list = solution.merge_k_lists([l1, l2, l3])

    print(solution.print_list(merged_list))

if __name__ == '__main__': main()