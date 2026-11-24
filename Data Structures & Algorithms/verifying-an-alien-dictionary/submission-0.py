class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}

        for i in range(len(order)):
            rank[order[i]] = i

        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i-1]))):

                if rank[words[i][j]] < rank[words[i-1][j]]:
                    return False

                elif rank[words[i][j]] > rank[words[i-1][j]]:
                    break

            else:
                if len(words[i]) < len(words[i-1]):
                    return False

        return True