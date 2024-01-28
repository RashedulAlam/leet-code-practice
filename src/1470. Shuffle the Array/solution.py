class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr1 = nums[:n]
        arr2 = nums[n:len(nums)]
        result = []
        for num1, num2  in zip(arr1, arr2):
            result.append(num1)
            result.append(num2)
        
        return result