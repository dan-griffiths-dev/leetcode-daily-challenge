


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        queue = []
        seen = set()
        while queue:   

            node = queue.pop()
            if k - node.val in seen:
                return True
            
            seen.add(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False
    



