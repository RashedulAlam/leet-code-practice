class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        
        max1 = nums.index(max(nums))
        min1 = nums.index(min(nums))
        
        length = len(nums)
        
        return min(max(max1 + 1, min1 + 1) , max(length - max1, length - min1) , (max1 + 1 + length - min1) , (min1 + 1 + length - max1))