class TreeNode:
    def __init__(self,val=None,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'T({self.val})'
    

class Solution:
    def is_same_tree(self,t1,t2):
        if t1 and t2:
            c1 = t1.val == t2.val
            c2 = self.is_same_tree(t1.left,t2.left)
            c3 = self.is_same_tree(t1.right,t2.right)
            return c1 and c2 and c3
        else:
            return t1 == t2

if __name__=='__main__':
    """
        1
       / \
      2   5
     / \  /
    3   4 6

         0
        /
        1
       / \
      2   5
     / \  /
    3   4 6
    """
    t1 = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6)))
    t2 = TreeNode(0,TreeNode(10,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6))))
    print(Solution().is_same_tree(t1,t2.left))
