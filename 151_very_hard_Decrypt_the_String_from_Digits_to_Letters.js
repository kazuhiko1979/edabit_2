/** / * Decrypt the String from Digits to Letters
 * Given a string s consisting of digits and #, translate s to English lowercase characters as follows:
 *
 * Characters ("a" to "i") are represented by ("1" to "9").
 * Characters ("j" to "z") are represented by ("10#" to "26#").
 */

function decrypt(s){
  /**
   * Decrypts the given string `s` using the provided rules.
   *
   * @param {string} s - The string to be decrypted.
   * @returns {string} The decrypted string.
   */

  const singleDigits = 'abcdefghi';
  const doubleDigits = 'jklmnopqrstuvwxyz';

  let result = '';
  let i = s.length -1;

  while (i >= 0){
    if (s[i] !== '#') {
      result = singleDigits[parseInt(s[i]) -1] + result;
      i--;
    } else {
      const num = parseInt(s.slice(i - 2, i));
      result = doubleDigits[num - 10] + result;
      i -= 3;
    }
  }

  return result;
  }


// Examples
console.log(decrypt("10#11#12")); // Output: jkab
console.log(decrypt("1326#")); // Output: acz
console.log(decrypt("25#")); // Output: y