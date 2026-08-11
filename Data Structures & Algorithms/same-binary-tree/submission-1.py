# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue.append([p,q])
        while queue:
            node1,node2 = queue.popleft()
            # print("outside",node1.val,node2.val)
            # if (not node1 and node2) or (not node2 and node1):
            #     return False
                
            # if node1.val != node2.val:
            #     print(node1.val,node2.val)
            #     return False

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            queue.append([node1.left,node2.left])
            queue.append([node1.right,node2.right])
            
            
        return True