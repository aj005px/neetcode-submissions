class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        temp = []

        for i in range(len(grid)):
            for j in range(len(grid)):
                temp.append(grid[i][j])

        temp.sort()

        repeated = 0
        missing = 0

        for i in range(1, len(temp)+1):
            if temp.count(i) > 1:
                repeated = i

            if i not in temp:
                missing = i

        return [repeated, missing]