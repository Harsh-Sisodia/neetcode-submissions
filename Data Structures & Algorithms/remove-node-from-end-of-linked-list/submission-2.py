# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        c = 0
        while tmp:
            c+=1
            tmp=tmp.next

        i = c - n
        tmp,prev = head,None
        if i==0:
            head = head.next
        else:
            while i!=0:
                prev = tmp
                tmp = tmp.next
                i-=1
            prev.next = tmp.next

        return head
