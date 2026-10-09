class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 1
        ans = 0
        while j<len(s):
            temp = abs(ord(s[i]) - ord(s[j]))
            ans+=temp
            i +=1
            j += 1
        return ans

