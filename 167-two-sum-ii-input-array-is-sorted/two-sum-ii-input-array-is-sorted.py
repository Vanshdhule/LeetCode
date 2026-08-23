class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        start = 0
        end = n - 1

        while start<end:
            total = numbers[start] + numbers[end]
            if total == target:
                return start+1,end+1
            elif total < target:
                start += 1
            else:
                end -= 1
                