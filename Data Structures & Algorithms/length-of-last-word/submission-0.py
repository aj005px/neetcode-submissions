class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = list(s)
        word = []
        temp = ''

        for i in l:
            if i == ' ':
                if temp != '':
                    word.append(temp)
                temp = ''
            else:
                temp += i

        if temp != '':
            word.append(temp)

        last = word[-1]
        return len(last)