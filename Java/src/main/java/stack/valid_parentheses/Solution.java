package stack.valid_parentheses;

import java.lang.reflect.Array;
import java.util.*;

public class Solution {
    public boolean isValid(String s) {
        int len = s.length();
        if (len % 2 != 0)
            return false;

        Stack<Character> stack = new Stack<>();
        stack.push(null);
        HashMap<Character, Character> pairs = new HashMap<>(
                Map.of(')', '(', ']', '[', '}', '{'));
        for (char c : s.toCharArray()) {
            Character value = pairs.get(c);
            if (value == null) {
                stack.push(c);
                continue;
            }
            if (value.equals(stack.lastElement()))
                stack.pop();
            else
                return false;
        }
        if (!(stack.lastElement() == null))
            return false;
        return true;
    }
}
