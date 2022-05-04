class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        queue.append(root)
        if root is None:
            return res
        while queue:
            size = len(queue)
            levelList = []
            for i in range(size):
                temp = queue.pop(0)
                levelList.append(temp.val)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
            res.append(levelList)
        return res