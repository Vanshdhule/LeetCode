class Solution(object):
    def isPalindrome(self, x):
        rev = 0
        org = x
        while x> 0:
            num = x % 10
            rev = rev * 10 + num
            x = x//10
        return rev == org
        