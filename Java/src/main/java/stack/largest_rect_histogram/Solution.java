package stack.largest_rect_histogram;

import java.util.Stack;

public class Solution {
    class Item {
        int index, height;
        public Item(int index, int height) {
            this.index = index;
            this.height = height;
        }
    }
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Stack<Item> stack = new Stack<>();
        for (int i = 0; i < heights.length; i++) {
            int start = i;
            while (!stack.isEmpty()
                    && stack.lastElement().height > heights[i]) {
                Item item = stack.pop();
                int area = item.height * (i - item.index);
                if (area > maxArea) {
                    maxArea = area;
                }
                start = item.index;
            }
            stack.push(new Item(
                    start,
                    heights[i]
            ));
        }

        for (Item item : stack) {
            int area = item.height * (heights.length - item.index);
            if (area > maxArea) {
                maxArea = area;
            }
        }

        return maxArea;
    }
}
