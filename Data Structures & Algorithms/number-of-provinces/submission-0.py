class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        seen = set()
        count = 0
        n = len(isConnected)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)

        def dfs(node):
            seen.add(node)

            for i in graph[node]:
                if i not in seen:
                    dfs(i)
        
        for i in range(n):
            if i not in seen:
                count+=1
                dfs(i)
        
        return count