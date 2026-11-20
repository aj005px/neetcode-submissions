class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_list = list(allowed)

        for i in words:
            temp = list(i)
            flag = True
            for char in temp:
                if char not in allowed_list:
                    flag = False
                    break

            if flag:
                count += 1

        return count