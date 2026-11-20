class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = []

        for i in set(words[0]):
            count = min(word.count(i) for word in words)

            for j in range(count):
                common.append(i)

        return common