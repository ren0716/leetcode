class Solution:
    def digitSum(self, s: str, k: int) -> str:
        temp = ''
        while len(s) > k:
            sm = 0
            curr_len = 0
            for idx, digit in enumerate(s):
                curr_len += 1
                sm += int(digit)

                if curr_len == k or idx == len(s) - 1:
                        temp += str(sm)
                        sm = 0
                        curr_len = 0
            s = temp
            temp = ''
        return s






        