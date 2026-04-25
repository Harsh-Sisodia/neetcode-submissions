class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for i in s:
            if i == ")" or i == "}" or i=="]":
                if stack == []:
                    return False
                
                top = stack[-1]
                if i==")" and top == "(":
                    stack.pop()
                elif i=="}" and top == "{":
                    stack.pop()
                elif i=="]" and top == "[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if stack==[]:
            return True
        else:
            return False
