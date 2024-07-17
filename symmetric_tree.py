class TreeNode:
    def __init__(self,val=None,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'T({self.val})'
    
class Solution:
    def is_symmetric_tree(self,t):
        def dfs(l,r):
            if l and r:
                c1 = l.val == r.val
                c2 = dfs(l.left,r.right)
                c3 = dfs(l.right,r.left)
                return c1 and c2 and c3
            else:
                return l == r
        return dfs(t,t)
    
if __name__=='__main__':
    """
        1
       / \
      2   2
    """
    t = TreeNode(1,TreeNode(2),TreeNode(2))
    print(Solution().is_symmetric_tree(t))