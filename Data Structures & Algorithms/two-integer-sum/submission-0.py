class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        ans=[0,0]
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in map:
                ans[0]=map[diff]
                ans[1]=i
                return ans
            else:
                map[nums[i]]=i
            print(map)
        return ans

        