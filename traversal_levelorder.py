from collections import deque

class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelorder(self, root):
        """
        Approach
        - Visit the node
        - Push the left subtree to queue
        - Push the right subtree to queue
        - Repeat until queue is empty
        """
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

if __name__=='__main__':
    """
        1
       / \
      2   5
     / \  /
    3   4 6
    """
    t = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6)))
    Solution().levelorder(t)
