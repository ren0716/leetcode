class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #maintain a table of num -> freq then heapify to maxheap and pop topk
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        #throw everything into a heap
        maxheap = []
        for key, value in freq.items():
            heapq.heappush(maxheap, (-value, key))
        
        #retrieve
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxheap)[1])
        
        return res


        