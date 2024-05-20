class Solution:
	def PowMod(self, x, n, m):
    if n==0:
      return 1
    if n==1:
      return x
    val = self.PowMod(x,n//2,m)
    val = (val*val)%m
    if n%2==1:
      val = (val*x)%m
    return val
