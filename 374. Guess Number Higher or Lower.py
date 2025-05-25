
class Solution(object):
    def guessNumber(self, n):
        start = 1
        end = n

        while start <= end:
            mid = start + (end - start) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                start = mid + 1
            elif g == -1:
                end = mid - 1
        return -1