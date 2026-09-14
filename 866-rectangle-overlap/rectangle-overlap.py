class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rec = [left, bottom, right, top]

        separated = (
            rec1[2] <= rec2[0] or  # rec1 is entirely left of rec2
            rec2[2] <= rec1[0] or  # rec2 is entirely left of rec1
            rec1[3] <= rec2[1] or  # rec1 is entirely below rec2
            rec2[3] <= rec1[1]    # rec2 is entirely below rec1
        )

        return not separated
        