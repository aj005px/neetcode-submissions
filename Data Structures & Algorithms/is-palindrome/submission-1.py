class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = list(s[::-1].lower())
        s2 = list(s.lower())
        k = ''
        for i in s1:
            if i not in 'qwertyuiopasdfghjklzxcvbnm0123456789':
                continue
            k += i
        
        l = ''
        for i in s2:
            if i not in 'qwertyuiopasdfghjklzxcvbnm0123456789':
                continue
            l += i
        return k == l
 