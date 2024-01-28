class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for index, num in enumerate(nums):
            sub_array = nums[index + 1 :len(nums)]
            print(sub_array)
            for num1 in sub_array:
                if num1 == num:
                    count += 1
                    
        return count