class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack)!= 0 and abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)