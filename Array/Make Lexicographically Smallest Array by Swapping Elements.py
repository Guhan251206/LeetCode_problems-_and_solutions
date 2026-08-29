from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        group=[]
        map={}
        for x in sorted(nums):
            if not group or x-group[-1][-1]>limit:
                group.append(deque())
            group[-1].append(x)
            map[x]=len(group)-1
        

        return [group[map[x]].popleft() for x in nums]