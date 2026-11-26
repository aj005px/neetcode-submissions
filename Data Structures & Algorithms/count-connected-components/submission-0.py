class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        counter = 0

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visit.add(node)
            for i in graph[node]:
                if i not in visit:
                    dfs(i)

        for i in range(n):
            if i not in visit:
                counter += 1
                dfs(i)

        return counter