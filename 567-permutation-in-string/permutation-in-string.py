class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0] * 26
        for char in s1:
            freq_s1[ord(char) - ord('a')] += 1
        
        #build a dynamic freq array for s2
        freq_s2 = [0] * 26
        start = 0
        for char in s2:
            
            pos = ord(char) - ord('a')
            freq_s2[pos] += 1
            
            # fix if no longer permutation
            while freq_s2[pos] > freq_s1[pos]:
                start_char = s2[start]
                start_pos = ord(start_char) - ord('a')
                freq_s2[start_pos] -= 1
                start += 1
            
            #check if permutation
            for i in range(26):
                    if freq_s2[i] != freq_s1[i]:
                        break
                    if i == 25:
                        return True
        return False
                
        