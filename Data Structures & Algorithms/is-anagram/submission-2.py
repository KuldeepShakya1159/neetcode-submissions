class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        if len(t) != len(s):
            return False

        for char in s:
            if char in hashMap:
                hashMap[char] = hashMap[char]+1
            else:
                hashMap[char]=1
        for char in t:
            if char in hashMap and hashMap[char]>0:
                hashMap[char] = hashMap[char]-1
            else:
                return False
        return True
        