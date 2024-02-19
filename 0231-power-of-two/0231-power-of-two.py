class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:return False
        if( log2(n)).is_integer():return True
        else:return False