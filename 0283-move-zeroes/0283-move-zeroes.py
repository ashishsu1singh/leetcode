class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
       l=0
       r=0
       while l<len(nums) and r< len(nums):
        while l< len(nums) and nums[l] !=0:
            l +=1
        while r<len(nums) and (nums[r] ==0 or r<l):
            r +=1
        if l < len(nums) and r <len(nums):
            nums[l],nums[r] = nums[r],nums[l]

        