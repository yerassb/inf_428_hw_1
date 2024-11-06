class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        maxc = count
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > prev:
                count += 1
            else:
                maxc = max(maxc, count)
                count = 1
            prev = nums[i]

        return max(maxc, count)