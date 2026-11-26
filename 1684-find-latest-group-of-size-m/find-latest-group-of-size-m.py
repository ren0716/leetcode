class Solution:
    def findLatestStep(self, arr: list[int], m: int) -> int:
        n = len(arr)
        parent = list(range(n))
        size = [0] * n
        active = [False] * n
        groups = 0
        answer = -1

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            nonlocal groups

            a, b = find(a), find(b)
            if a == b:
                return

            # These exact-size groups cease to exist when merged.
            if size[a] == m:
                groups -= 1
            if size[b] == m:
                groups -= 1

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

            if size[a] == m:
                groups += 1

        for step, position in enumerate(arr, 1):
            p = position - 1
            active[p] = True
            size[p] = 1

            if m == 1:
                groups += 1

            for neighbor in (p - 1, p + 1):
                if 0 <= neighbor < n and active[neighbor]:
                    union(p, neighbor)

            if groups > 0:
                answer = step

        return answer