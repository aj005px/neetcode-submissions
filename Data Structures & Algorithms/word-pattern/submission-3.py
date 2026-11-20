class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = {}
        pat = set()
        split = s.split()

        if len(pattern) != len(split):
            return False

        for i in range(len(split)):
            if pattern[i] not in pat:
                pat.add(pattern[i])

            if pattern[i] not in match:
                match[pattern[i]] = split[i]

            if pattern[i] in pat:
                if match[pattern[i]] != split[i]:
                    return False

        if len(set(match.values())) != len(match):
            return False

        return True