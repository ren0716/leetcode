class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #check both top left and bottom right for rec1, rec2 and rec2, rec1 respectively
        #do the same for bottom left and top right
        rec1_bl = (rec1[0], rec1[1])
        rec1_tr = (rec1[2], rec1[3])
        rec2_bl = (rec2[0], rec2[1])
        rec2_tr = (rec2[2], rec2[3])
        #derive top left and bottom right
        rec1_br = (rec1[2], rec1[1])
        rec1_tl = (rec1[0], rec1[3])
        rec2_br = (rec2[2], rec2[1])
        rec2_tl = (rec2[0], rec2[3])

        if rec1_bl[0] < rec2_tr[0] and rec1_bl[1] < rec2_tr[1] and rec1_tr[0] > rec2_bl[0] and rec1_tr[1] > rec2_bl[1]:
            return True
        
        if rec2_bl[0] < rec1_tr[0] and rec2_bl[1] < rec1_tr[1] and rec2_tr[0] > rec1_bl[0] and rec2_tr[1] > rec1_bl[1]:
            return True
        
        return False
        