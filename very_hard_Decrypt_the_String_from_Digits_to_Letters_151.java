/**
 * Decrypt the String from Digits to Letters
 * Given a string s consisting of digits and #, translate s to English lowercase characters as follows:
 *
 * Characters ("a" to "i") are represented by ("1" to "9").
 * Characters ("j" to "z") are represented by ("10#" to "26#").
 */
public class very_hard_Decrypt_the_String_from_Digits_to_Letters_151 {
  public static String decrypt(String s) {
      /**
       * Decrypts the given string `s` using the provided rules.
       *
       * @param s - The string to be decrypted.
       * @return The decrypted string.
       */
      String singleDigits = "abcdefghi";
      String doubleDigits = "jklmnopqrstuvwxyz";

      StringBuilder result = new StringBuilder();
      int i = s.length() - 1;

      while (i >= 0) {
          if (s.charAt(i) != '#') {
              result.insert(0, singleDigits.charAt(Integer.parseInt(String.valueOf(s.charAt(i))) - 1));
              i--;
          } else {
              int num = Integer.parseInt(s.substring(i - 2, i));
              result.insert(0, doubleDigits.charAt(num - 10));
              i -= 3;
          }
      }

      return result.toString();
  }

  public static void main(String[] args) {
      // Examples
      System.out.println(decrypt("10#11#12")); // Output: jkab
      System.out.println(decrypt("1326#")); // Output: acz
      System.out.println(decrypt("25#")); // Output: y
  }
}