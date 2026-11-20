class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        stack = []
        stack.append(0)
        while len(stack) > 0:
            curr = stack.pop()
            keys = rooms[curr]
            for key in keys:
                if key not in visited:
                    stack.append(key)
            visited.add(curr)
        
        return len(visited) == len(rooms)

                    
        