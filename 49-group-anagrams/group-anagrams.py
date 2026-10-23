class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #anagram check with freq tuple
        seen = {}
        for string in strs:
            freq_list = [0] * 26
            for char in string:
                pos = ord(char) - ord('a')
                freq_list[pos] += 1

            freq_tuple = tuple(freq_list)
            if freq_tuple in seen:
                seen[freq_tuple].append(string)
            else:
                seen[freq_tuple] = [string]

        #return results from table
        res = []
        for _, value in seen.items():
            res.append(value)

        return res 

        