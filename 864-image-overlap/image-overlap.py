class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        #hash both the array
        rows = len(img1)
        cols = len(img1[0])
        table1 = []
        table2 = []
        for row in range(rows):
            for col in range(cols):
                if img1[row][col] == 1:
                    table1.append((row, col))
                if img2[row][col] == 1:
                    table2.append((row, col))
        
        shifts = defaultdict(int)
        largest = 0
        for r1, c1 in table1:
            for r2, c2 in table2:
                shift = (r1 - r2, c1 - c2)
                shifts[shift] += 1
                largest = max(shifts[shift], largest)
        
        return largest

        



        