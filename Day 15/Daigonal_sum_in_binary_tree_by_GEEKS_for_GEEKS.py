# Problem Statement: Diagonal Sum in Binary tree
class Solution:
    #Complete the function below
    def diagonalSum(self, root):
        list = []
        queue = []
        sum = 0
        count = 0
        last = 0
        while (root != None):
            if (root.left != None):
                queue.append(root.left)
                count += 1
            sum += root.data
            root = root.right
            if (root == None):
                if (len(queue) != 0):
                    root = queue.pop(0)
                if (last == 0):
                    list.append(sum)
                    sum = 0
                    last = count
                    count = 0
                last -= 1
        return list
