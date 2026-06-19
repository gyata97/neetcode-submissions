class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def bfs(node):
            queue = deque([node])
            visited.add(node)

            while queue:
                cur = queue.popleft()
                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return None

        count = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                count += 1

        return count