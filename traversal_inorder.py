class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root):
        """
        Approach
        - Visit the node
        - Visit the left subtree
        - Visit the right subtree
        """
        if root: 
            print(root.val)
            self.inorder(root.left)
            self.inorder(root.right)

if __name__=='__main__':
    """
        1
       / \
      2   5
     / \  /
    3   4 6
    """
    t = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6)))
    Solution().inorder(t)