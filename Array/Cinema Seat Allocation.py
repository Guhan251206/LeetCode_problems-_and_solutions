class Solution:
    def maxNumberOfFamilies(self, n: int, re: List[List[int]]) -> int:
        reserved = {}

        for row, seat in re:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        count = (n - len(reserved)) * 2

        for row in reserved:
            seats = reserved[row]

            left = all(s not in seats for s in [2, 3, 4, 5])
            right = all(s not in seats for s in [6, 7, 8, 9])
            middle = all(s not in seats for s in [4, 5, 6, 7])

            if left and right:
                count += 2
            elif left or right or middle:
                count += 1

        return count