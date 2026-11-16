class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        #modulo math mod(a + b) = mod(mod(a) + mod(b))
        #subarrays and sum -> prefix sum for O(1) 
        #(O(n^2)
        #can use prefix_parity count so i only need to do O(n) scan
        MOD = 10**9 + 7
        acc = 0
        even = 1
        odd = 0
        pref_sum = 0
        for num in arr:
            pref_sum += num
            contribution = None
            if pref_sum % 2 == 0:
                even += 1
                contribution = odd
            else:
                odd += 1
                contribution = even
            acc = (acc + contribution) % MOD



        return acc 
        

        