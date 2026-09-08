class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for num in nums:
            map[num] = map.get(num, 0) + 1
        for n, c in map.items():
            frequency[c].append(n)
        
        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res

        