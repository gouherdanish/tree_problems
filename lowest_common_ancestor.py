class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'TreeNode({self.val})'

class Solution:
    def lca(self, root, p, q):
        """
        Approach - Inorder Traversal (Recursive)
        - Start from root, search for p and q in left tree and right tree
        - Say if p is found is left tree and q is found in right tree (both l and r are not not None), then current node is LCA
        - if both p and q are not found in the left subtree, then both must be present in the right subtree,
            in which case whichever is found earlier in the right subtree must be the LCA

        Analysis:
            T(n)    = 2T(n/2) + O(1) 
                    = 2(2T(n/4) + O(1)) + O(1) = 4T(n/4) + 2*O(1) + O(1)
                    = 8T(n/8) + 4*O(1) + 2*O(1) + O(1)
                    = 2^k * T(n/2^k) + 2^(k-1)*O(1) + .... + 4*O(1) + 2*O(1) + O(1)
                    = (2^(k+1) - 1) / (2-1)
                    = 2^k
                    = n
            Time    = O(n)
        """
        def dfs(node, p, q):
            if not node: return None
            if node.val == p or node.val == q: return node
            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)
            if l and r: return node
            return l or r
        return dfs(root, p, q)
    

class Solution1:
    def lca(self, root, p, q):
        """
        Approach - Level Order (Iterative)
        - Go level by level and keep track of each node's parent
        - Loop until p and q have same ancestor

        Time - O(n)
        """
        from collections import deque
        qu = deque()
        parent = {root.val:None}
        qu.append(root)
        while qu:
            node = qu.popleft()
            if node.left:
                qu.append(node.left)
                parent[node.left.val] = node.val
            if node.right:
                qu.append(node.right)
                parent[node.right.val] = node.val
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q:
            if q in ancestors: return q
            q = parent[q]

if __name__=='__main__':
    """
        1
       / \
      2   5
     / \  /
    3   4 6
    """
    t = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6)))
    # print(Solution1().lca(t,2,6))    # 1
    # print(Solution1().lca(t,3,4))    # 2
    print(Solution1().lca(t,2,4))    # 2
    