class Solution(object):
    def removeDuplicates(self, nums):
        low = 0
        high = 1
        
        while high < len(nums):
            if nums[high] == nums[high - 1]:
                high += 1
            else: 
                nums[low + 1] = nums[high]
                low += 1
                high += 1
        return low + 1 