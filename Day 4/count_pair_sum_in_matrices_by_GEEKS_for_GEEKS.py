# problem Statement : Count pairs Sum in matrices

class Solution:
	def countPairs(self, mat1, mat2, n, x):
	    
	    count = 0
	    i=0
	    j=0
	    p=n-1
	    q=n-1
	    
	    while i<n and p>=0:
	        sum = mat1[i][j]+mat2[p][q]
	        if sum == x:
	            count += 1
	            j =j+1
	            q -= 1
	        elif sum > x:
	            q -= 1
	        elif sum<x:
	            j += 1
	        if q == -1:
	            q = n-1
	            p -= 1
	        if j==n:
	            j=0
	            i+=1
        return count

  
  # work fine but time complexity is more
	            
	   # c=0  
	   # for i in sum(mat1, []): #conversion of 2D array in 1D array
	   #     for j in sum(mat2, []):
	   #         if i+j==x:
	   #             c+=1
	   # return c
