class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		nuts.sort(key=ascii)
		bolts.sort(key=ascii)
		return nuts,bolts
