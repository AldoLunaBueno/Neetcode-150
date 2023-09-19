package two_pointers.valid_palindrome;

public class Solution {
    public boolean isPalindrome(String s) {
        char[] chars = s.toLowerCase().toCharArray();

        int ptrStart = 0, ptrEnd = chars.length -1;
        while (ptrStart < ptrEnd) {
            while (!Character.isLowerCase(chars[ptrStart])
                    && !Character.isDigit(chars[ptrStart])
                    && ptrStart < ptrEnd) {
                ptrStart++;
            }
            while (!Character.isLowerCase(chars[ptrEnd])
                    && !Character.isDigit(chars[ptrEnd])
                    && ptrStart < ptrEnd) {
                ptrEnd--;
            }
            if (chars[ptrStart] != chars[ptrEnd]) {
                return false;
            }
            ptrStart++;
            ptrEnd--;
        }
        return true;
    }
}
