class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if len(stack)==0:
                    return False
                else:
                    temp=stack.pop(-1)
                    if not ((i==')' and temp=="(") or (i=="}" and temp=="{") or (i=="]" and temp=="[")):
                        return False


        if len(stack)==0:
            return True
        else:
            return False



      