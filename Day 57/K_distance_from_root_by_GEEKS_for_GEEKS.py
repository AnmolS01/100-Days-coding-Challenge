class Solution:
    def KDistance(self,root,k):
        '''
        :param root: root of given tree.
        :param k: distance k from root
        :return: list of all nodes that are at distance k from root.
        '''
        # code here
        result = []
        def findKDistance(root, k):
            if root is None:
                return
            if k == 0:
                result.append(root.data)
                return
            findKDistance(root.left, k - 1)
            findKDistance(root.right, k - 1)
        findKDistance(root, k)
        return result
