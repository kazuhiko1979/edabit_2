import java.util.HashMap;
import java.util.Map;

public class very_hard_Roman_Numerals_163 {

    public static int parseRomanNumeral(String roman) {
        Map<Character, Integer> romanNumerals = new HashMap<>();
        romanNumerals.put('I', 1);
        romanNumerals.put('V', 5);
        romanNumerals.put('X', 10);
        romanNumerals.put('L', 50);
        romanNumerals.put('C', 100);
        romanNumerals.put('D', 500);
        romanNumerals.put('M', 1000);

        int total = 0;
        int prevValue = 0;

        for (int i = roman.length() - 1; i >= 0; i--) {
            char ch = roman.charAt(i);
            int value = romanNumerals.get(ch);

            if (value < prevValue) {
                total -= value;
            } else {
                total += value;
            }
            prevValue = value;
        }

        return total;
    }

    public static void main(String[] args) {
        // Example test cases
        System.out.println(parseRomanNumeral("I"));           // ➞ 1
        System.out.println(parseRomanNumeral("VIII"));        // ➞ 8
        System.out.println(parseRomanNumeral("XXIX"));        // ➞ 29
        System.out.println(parseRomanNumeral("LIV"));         // ➞ 54
        System.out.println(parseRomanNumeral("CCV"));         // ➞ 205
        System.out.println(parseRomanNumeral("CDXLIV"));      // ➞ 444
        System.out.println(parseRomanNumeral("CMXCIX"));      // ➞ 999
        System.out.println(parseRomanNumeral("M"));           // ➞ 1000
        System.out.println(parseRomanNumeral("MMMDCCCLXXXVIII"));  // ➞ 3888
        System.out.println(parseRomanNumeral("MMMCMX"));      // ➞ 3910
    }
}
