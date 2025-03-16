class Solution(object):
    def reverseString(self, s):
        l, r = 0, len(s) - 1  

        while l < r:
            s[l], s[r] = s[r], s[l]  
            l += 1
            r -= 1  


s1 = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s1)  