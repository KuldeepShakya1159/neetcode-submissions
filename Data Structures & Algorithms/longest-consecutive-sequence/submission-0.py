class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        startArr = []
        maxLen=0
        if len(nums)==0:
            return 0

        for num in hashSet:
            if num-1 not in hashSet:
                startArr.append(num)

        for i in range(len(startArr)):
            count=1
            currentStart=startArr[i]
            while(currentStart+1 in hashSet):
                count+=1
                currentStart+=1
            maxLen = max(maxLen,count)
        
        return maxLen
