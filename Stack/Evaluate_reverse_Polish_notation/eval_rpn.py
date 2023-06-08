from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for a in tokens:
            try:
                a = int(a)
                stack.append(a)        
            except ValueError:
                n = stack.pop() 
                m = stack.pop()
                res = 0
                if a == "+":
                    res = m + n
                elif a == "-":
                    res = m - n
                elif a == "*":
                    res = m * n
                elif a == "/":
                    res = int(m / n)
                stack.append(res)                
        return stack.pop()