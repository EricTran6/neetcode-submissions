class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        res = []
        for i, n in enumerate(nums):
            right_sum = total_sum - left_sum - n

            left_size, right_size = i, len(nums) - 1 - i

            res.append(
                left_size * n - left_sum + right_sum - right_size * n
            )

            left_sum += n
        return res

        

