class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opps = { ")" : "(", "]" : "[", "}" : "{" }
        
        for c in s:
            if c in opps:
                if not stack:
                    return False
                if stack.pop() != opps[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

