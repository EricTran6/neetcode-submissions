class Solution:
    def minimumDeletions(self, s: str) -> int:
        counts = Counter(s)
        a_count = counts["a"]

        b_count = 0
        res = len(s)
        for idx, char in enumerate(s):
            if char == "a":
                a_count -= 1
            res = min(res, a_count + b_count)
            if char == "b":
                b_count += 1
        return res

#abbabab