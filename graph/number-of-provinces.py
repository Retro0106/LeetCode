from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        numComponents = 0
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    graph[i+1].append(j+1)

        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                     dfs(neighbor)
            return  

        
        
        for node in range(1, n+1):
            if node not in visited:
                numComponents += 1
                dfs(node)

        return numComponents
      
                    