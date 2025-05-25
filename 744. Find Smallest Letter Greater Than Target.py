class Solution(object):
    def nextGreatestLetter(self, letters, target):

        low = 0
        high = len(letters) - 1
        a = letters[0]

        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                a = letters[mid]
                high = mid - 1
            else:
                low = mid + 1

        return a