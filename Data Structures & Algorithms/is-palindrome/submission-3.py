class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.replace(" ","").strip().lower()
        i=0
        j=len(lowerS)-1

        while(i<j):
            while i<j and not (ord('a')<=ord(lowerS[i])<=ord('z')
                or ord('0')<=ord(lowerS[i])<=ord('9')):
                i+=1
            while i<j and not (ord('a')<=ord(lowerS[j])<=ord('z')
                 or ord('0')<=ord(lowerS[j])<=ord('9')):
                j-=1
            if lowerS[i]!=lowerS[j]:
                return False
            else:
                i+=1
                j-=1
        return True

        