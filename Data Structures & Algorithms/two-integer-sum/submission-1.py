class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        res = []
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in map:
                return [map[diff], idx]
            map[val] = idx
        return []
