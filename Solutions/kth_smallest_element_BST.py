def dfs(self, root, stack):
    if root.left != None:
        dfs(self, root.left, stack)
    stack.append(root.val)
    if root.right != None:
        dfs(self, root.right, stack)
    
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        dfs(self, root, stack)
        return stack[k-1]