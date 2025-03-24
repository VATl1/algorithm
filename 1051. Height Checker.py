class Solution(object):
    def heightChecker(self, heights):
        a = sorted(heights)
        l = 0
        for i in range(len(heights)):
            if heights[i] != a[i]:
                l+=1
        return l 