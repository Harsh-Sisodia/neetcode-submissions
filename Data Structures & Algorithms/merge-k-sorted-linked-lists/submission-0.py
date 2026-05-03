# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in lists:
            while i:
                arr.append(i.val)
                i=i.next
        arr.sort()
        
        # print(arr)
        if not arr:
            return 
        dummy = ListNode(arr[0])
        head = dummy
        for i in range(1,len(arr)):
            dummy.next = ListNode(arr[i])
            dummy = dummy.next
        return head
