# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Nwrap:
    def __init__(self,node):
        self.node = node
    def __lt__(self,other):
        return self.node.val<other.node.val 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        
        res = ListNode(-1)
        cur = res 
        minheap = []

        for i in lists:
            if i is not None:
                heapq.heappush(minheap, Nwrap(i))

        while minheap:
            nodew = heapq.heappop(minheap)
            cur.next = nodew.node
            cur = cur.next 

            if nodew.node.next:
                heapq.heappush(minheap, Nwrap(nodew.node.next))
        
        return res.next