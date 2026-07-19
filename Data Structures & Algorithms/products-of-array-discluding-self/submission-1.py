class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        pres = [1] * len(arr)
        succf = [1] * len(arr)

        for i in range(len(arr)):
            pres[i] = arr[i] * (pres[i-1] if i>0 else 1)

        for i in range(len(arr)-1,-1,-1):
            succf[i] = arr[i] * (succf[i+1] if i+1!=len(arr) else 1)

        sol =[1]*len(arr)

        for i in range(len(arr)):
            if i>0 and i+1<len(arr):
                sol[i] = pres[i-1]*succf[i+1]
            elif i==0:
                sol[i] = succf[i+1] 
            else:
                sol[i] = pres[i-1]
        return sol
        