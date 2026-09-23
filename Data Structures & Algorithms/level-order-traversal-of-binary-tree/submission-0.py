# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(node, level):
            if not node:
                return
            
            # If we are visiting a new level for the first time, 
            # create a new list for it in our answer array
            if len(ans) == level:
                ans.append([])
            
            # Add the current node's value to its corresponding level list
            ans[level].append(node.val)
            
            # Go deeper into left and right children, increasing the level by 1
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        return ans

        