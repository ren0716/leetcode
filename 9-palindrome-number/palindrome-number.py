class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        #use // to find length
        base = 10
        length = 0
        curr = x
        while curr != 0:
            curr = curr // base
            length += 1
        #mod to extract lower position
        left = 10
        #floor division to extract first element
        right = pow(10, length - 1)
        while left <= right:
            highest = int(x // (right))
            lowest = int((x % left) // (left // 10))
            if highest != lowest:
                return False
            #update left, right, x
            left *= 10
            x = x - (right * highest)
            right /= 10
            
        
        return True



        