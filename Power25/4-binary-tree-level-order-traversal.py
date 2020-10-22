# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        total_nodes = []
        
        queue = deque([root])
        
        while len(queue) != 0:
            level_len = len(queue)
            level_nodes = []
            for i in range(level_len):
                cur_node = queue.popleft()
                level_nodes.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            total_nodes.append(level_nodes)
        
        return total_nodes
