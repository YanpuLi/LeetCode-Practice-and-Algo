class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
            
        num = nums[0]
        for item in nums[1:]:
            if num == item:
                nums.remove(item)
            else:
                num = item
            
                
        return len(nums)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return len(nums)  
        last = nums[-1] 
        # as len is decreasing, start from last to first 
        for index in range(len(nums)-2,-1,-1):  
            if last == nums[index]: del nums[index]  
            else: last = nums[index]  
        return len(nums) 