from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            exact[d] = cnt[d] * (cnt[d] - 1) // 2
            for multiple in range(2 * d, mx + 1, d):
                exact[d] -= exact[multiple]

       
        prefix = [0] * (mx + 1)
        for d in range(1, mx + 1):
            prefix[d] = prefix[d - 1] + exact[d]

        ans = []
        for q in queries:
            ans.append(bisect_left(prefix, q + 1))

        return ans