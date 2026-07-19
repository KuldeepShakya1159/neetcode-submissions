class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in hashMap:
                hashMap[sortedS].append(s)
            else:
                hashMap[sortedS] = [s]
        ans=[]
        for val in hashMap.keys():
            ans.append(hashMap[val])
        return ans
        