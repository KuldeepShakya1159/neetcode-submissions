class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0] *2
        hashMap = {}

        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                ans[0] = hashMap[target-nums[i]]
                ans[1] = i
                return ans
            else:
                hashMap[nums[i]] = i
        return ans



        