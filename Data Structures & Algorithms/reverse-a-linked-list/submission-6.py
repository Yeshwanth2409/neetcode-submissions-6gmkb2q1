# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L = None
        R = head

        while R != None:
            temp = R.next
            R.next = L
            L = R
            R = temp
        return L