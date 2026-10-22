# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #walk and get 2 halves around breakpoint
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        first, second = head, head
        for _ in range((1 + length) // 2):
            second = second.next
        
        #reverse second
        prev = None
        curr = second

        while curr:
            next_node = curr.next  # save the rest of the list
            curr.next = prev       # reverse this link
            prev = curr
            curr = next_node

        second = prev  # new head of the reversed second list
        
        #null the pointer to second portion
        for _ in range((length + 1) // 2 - 1):
            head = head.next
        head.next = None

        #zip them
        res = ListNode()
        turn = 0
        curr = res
        while first or second:
            if turn == 0:
                curr.next = first
                first = first.next
                curr = curr.next
            else:
                curr.next = second
                second = second.next
                curr = curr.next

            turn += 1
            turn %= 2
        
        return res.next







        