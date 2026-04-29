# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        i,j = 0,len(arr)-1
        new = []
        while i<=j:
            if i==j:
                new.append(arr[i])
            else:
                new.append(arr[i])
                new.append(arr[j])
            i+=1
            j-=1
        temp = head
        i=0
        while temp:
            temp.val=new[i]
            i+=1
            temp=temp.next
        

                
            

            