# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         # finding middle 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
       
        # reversing the second half
        second = slow.next
        slow.next = prev = None

        while second:
            tmp = second.next
            second.next=prev
            prev = second
            second = tmp
        sec = prev

        # merging the reversed and first half

        fir = head
        

        while sec:
            tmp1 = fir.next
            tmp2 = sec.next

            fir.next=sec
            sec.next=tmp1

            fir,sec=tmp1,tmp2
            



         
