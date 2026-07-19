class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2!=0:
            return False

        stack = []

        for i in range(len(s)):
            if s[i]=='(' or s[i] == '{' or s[i] =='[':
                stack.append(s[i])
            else:
                topChar = stack[-1] if len(stack)>0 else ''
                if s[i] == ')' and topChar == '(':
                    stack.pop()
                elif s[i] == '}' and topChar == '{':
                    stack.pop()
                elif s[i] == ']' and topChar == '[':
                    stack.pop()
                else:
                    return False
        print(stack)
        return len(stack)==0
        