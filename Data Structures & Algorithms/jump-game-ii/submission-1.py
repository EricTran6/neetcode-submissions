class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        L, R = 0, 0
        res = 0
        while R < (len(nums) - 1):
            for i in range(L, R + 1):
                farthest = max(farthest, i + nums[i])
            L = R + 1
            R = farthest
            res += 1
        return res
