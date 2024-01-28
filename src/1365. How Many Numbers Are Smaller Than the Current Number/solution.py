class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for index, num in enumerate(nums):
            smaller_count = 0
            for index2,num2 in enumerate(nums):
                if index != index2 and nums[index2] < nums[index]:
                    smaller_count += 1
            result.append(smaller_count)
        
        return result
        