from typing import List
from bisect import bisect
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            stack.append([i, h])
            curr_

            if h < stack[-1][1]:
                prev_i, h = stack.pop()
                curr_area = (i - prev_i) * h