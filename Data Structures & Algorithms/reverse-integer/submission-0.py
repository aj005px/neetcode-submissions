class Solution:
    def reverse(self, x: int) -> int:
        res = abs(x)
        res = int(str(res)[::-1])
        if x<0:
            res = res*-1
        if res>2**31 or res<-2**31:
            return 0
        return res
