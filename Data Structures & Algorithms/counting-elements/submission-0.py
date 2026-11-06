class Solution:
    def countElements(self, arr: List[int]) -> int:
        sortedArr = set(sorted(arr))
        count = 0
        for i in range(len(arr)):
            if arr[i] + 1 in sortedArr:
                count += 1
        return count