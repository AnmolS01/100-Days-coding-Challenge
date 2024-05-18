class Solution:
	def findPeakElement(self, a):
		# Code here
		if not a:
		    return 0
		    
		n = len(a)
		start = 0
		end = n-1 
		
		while start < end:
		    mid = (start + end)//2
		    if a[mid] < a[mid+1]:
		        start = mid+1
		    else:
		        end = mid
		# this is because if we reach start == end then while loop breaks,
        # and we stand at max value.      
	    return a[start] 
