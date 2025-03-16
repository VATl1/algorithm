class Solution(object):
    def frequencySort(self, nums):
        count = Counter(nums)
        elements = list(count.keys())
        elements.sort(key=lambda x: (count[x], -x))
        result = []
        for num in elements:
            result += [num] * count[num]
        return result