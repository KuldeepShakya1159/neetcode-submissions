class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for n in nums:
            if hashset.get(n):
                return True
            else:
                hashset[n] = 1
        return False

        