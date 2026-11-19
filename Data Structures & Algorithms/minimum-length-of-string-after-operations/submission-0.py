class Solution:
    def minimumLength(self, s: str) -> int:
        counts = Counter(s)
        res = 0
        for cnt in counts.values():
            if cnt % 2 == 0:
                res += 2
            else:
                res += 1
        return res
