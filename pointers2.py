https://leetcode.com/problems/rotate-array

class Solution(object):
    def rotate(self, nums, k):

        nums=nums[len(nums)-k::]+nums[0:len(nums)-k]
       
        return nums

obj=Solution()
x=[1,2,3,4,5,6,7,8]
print(obj.rotate(x,3)) 
