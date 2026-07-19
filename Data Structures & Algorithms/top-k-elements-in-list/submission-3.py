class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map={}
        freqArr=[[]] * (len(nums)+1)

        for n in nums:
            if n in map:
                map[n] = map[n]+1
            else:
                map[n]=1
        
        for key,value in map.items():
            if len(freqArr[value])>0:
                tempArr = freqArr[value]
                tempArr.append(key)
                freqArr[value]=tempArr
            else:
                freqArr[value]=[key]
        solArr=[]
        
        for i in range(len(freqArr)-1,0,-1):
            if len(freqArr[i])>0:
                for s in freqArr[i]:
                    solArr.append(s)
                    if len(solArr)==k:
                        return solArr
        return solArr



                