class Solution:
    def findMin(self, nums: List[int]) -> int:

        r=len(nums)-1
        l=0

        if nums[l]<nums[r] or len(nums)==1:
            return nums[l]
        
        while r>0:
            if nums[r] > nums[r-1]:
                r-=1
            else:
                return nums[r]

        