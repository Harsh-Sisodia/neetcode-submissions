# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        tmp = head
        while tmp:
            arr.append(tmp.val)
            tmp=tmp.next
        
        a = len(arr)-n
        arr.pop(a)
        
        if not arr:
            return None
        tmp = head
        prev = None
        # print(arr)
        for i in arr:
            head.val = i
            prev = head
            head=head.next
        if prev:
            prev.next = None
        return tmp