# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        res = []

    
        while q:
            l = len(q)
            lev = []
            for i in range(l):
                node = q.pop(0)
                if node:
                    lev.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lev:
                res.append(lev)

        return res