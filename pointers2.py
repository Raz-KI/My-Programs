class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums=nums[len(nums)-k::]+nums[0:len(nums)-k]
        # s=nums[k+1:len(nums)+1]
        # s=s+nums[:k+1]
        # nums=s
        return nums

obj=Solution()
x=[1,2,3,4,5,6,7,8]
print(obj.rotate(x,3)) 