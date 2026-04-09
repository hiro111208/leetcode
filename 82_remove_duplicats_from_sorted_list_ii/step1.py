# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        current = dummy
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                tmp = current.next
                while tmp and tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
                current.next = tmp.next
                continue
            current = current.next
        return dummy.next
