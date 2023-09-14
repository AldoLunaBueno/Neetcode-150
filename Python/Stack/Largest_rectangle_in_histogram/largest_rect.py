from typing import List
from bisect import bisect
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                i_stack, h_stack = stack.pop()
                maxArea = max(maxArea, h_stack * (i - i_stack))
                start = i_stack # Guarda el índice del último elemento del stack eliminado
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea