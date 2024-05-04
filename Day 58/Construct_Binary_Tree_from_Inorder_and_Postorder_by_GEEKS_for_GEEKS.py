class Solution:
    def buildTreeUtil(self, inorder, postorder, inStart, inEnd, postStart, postEnd):
        if inStart > inEnd:
            return None
        
        rootValue = postorder[postEnd]
        root = Node(rootValue)
        
        rootIndex = inorder.index(rootValue)
        
        root.left = self.buildTreeUtil(inorder, postorder, inStart, rootIndex - 1, postStart, postStart + rootIndex - inStart - 1)
        root.right = self.buildTreeUtil(inorder, postorder, rootIndex + 1, inEnd, postStart + rootIndex - inStart, postEnd - 1)
        
        return root
    
    def buildTree(self, inorder, postorder, n):
        if not inorder or not postorder:
            return None
        
        return self.buildTreeUtil(inorder, postorder, 0, n - 1, 0, n - 1)
