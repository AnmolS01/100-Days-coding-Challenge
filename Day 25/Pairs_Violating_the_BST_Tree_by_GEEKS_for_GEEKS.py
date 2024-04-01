class Solution:
    def pairsViolatingBST(self, n: int, root: Optional['Node']) -> int:
        count = 0
        inorderList = []
        
        def inOrder(root):
            nonlocal inorderList
            if not root:
                return
            inOrder(root.left)
            inorderList.append(root.data)
            inOrder(root.right)
        
        inOrder(root)
      
        def merge_sort(arr):
            nonlocal count 
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]

                merge_sort(L)
                merge_sort(R)

                i = 0
                j = 0
                k = 0

                while i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                        count += len(L) - i
                    k += 1

                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
        
        merge_sort(inorderList)
        
        return count
