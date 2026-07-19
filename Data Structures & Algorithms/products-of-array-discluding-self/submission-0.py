class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        prod = 1
        numOfZeros=0
        for n in arr:
            if n==0:
                numOfZeros+=1
                if numOfZeros==2:
                    prod=0
                    break
                pass
            else:
                prod *= n 
        if prod==0:
            return [0] * len(arr)
        if numOfZeros==1:
            for i in range(len(arr)):
                if arr[i] ==0:
                    arr[i]=prod
                else:
                    arr[i]=0
        else:
            for i in range(len(arr)):
                arr[i]=int(prod/arr[i])
        return arr
        
        