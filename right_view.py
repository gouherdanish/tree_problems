class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.val}'
    
class Solution:
    def rightView(self, root):
        """
        Approach - Level Order
        - Go level by level and track the last elem

        Time - O(n) - we need to access each elem exactly once
        Space - O(n) - the max elems that queue has is from the last level (n/2)
        """
        if not root: return []
        from collections import deque
        q = deque()
        q.append(root)
        ans = []
        while q:
            qsize = len(q)
            for i in range(qsize):
                node = q.popleft()
                if i== qsize-1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

if __name__=='__main__':
    # t = TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3,None,TreeNode(4)))
    # t = TreeNode(1,None,TreeNode(3))
    t = None
    print(Solution().rightView(t))