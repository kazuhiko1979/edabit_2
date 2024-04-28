class very_hard_Maximum_Score_From_Two_Parts_of_a_String_152 {
  public int maxScore(String s){
    int zeros = 0;
    int ones = 0;
    for (char c : s.toCharArray()) {
      if (c == '1'){
        ones++;
      }
    }
    int maxSum = zeros + ones;
    for (char c : s.toCharArray()) {
        if (c == '0') {
          zeros++;
          ones--;
        } else {
          int temp = zeros + ones;
          maxSum = Math.max(maxSum, temp);
        }
    }
    return maxSum;
  }

public static void main(String[] args) {
  very_hard_Maximum_Score_From_Two_Parts_of_a_String_152 solution = new very_hard_Maximum_Score_From_Two_Parts_of_a_String_152();
  System.out.println(solution.maxScore("011101")); // 4
  System.out.println(solution.maxScore("00111")); // 5
  System.out.println(solution.maxScore("1111")); // 3
  System.out.println(solution.maxScore("00")); // 0
  System.out.println(solution.maxScore("01001")); // 4
  System.out.println(solution.maxScore("010101010101010101")); // 10
  System.out.println(solution.maxScore("01")); // 1
  System.out.println(solution.maxScore("1110010101")); // 5
  System.out.println(solution.maxScore("10")); // 1
  System.out.println(solution.maxScore("1100110010010111100000111001000111101111100011100111001101010100011001000000001111000000010000111101")); // 25
  // 他の長い例のテストケースは省略
  }
}