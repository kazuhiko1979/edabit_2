public class very_hard_Sum_the_Digits_of_All_Integers_0_to_10_n_1_155 {
  public static int sumDigitsInRange(int n){
    if (n == 0) return 0;
    return 45 * (int)Math.pow(10, n - 1) + 10 * sumDigitsInRange(n - 1);
  }

  public static void main(String[] args) {
    System.out.println(sumDigitsInRange(1));
    System.out.println(sumDigitsInRange(2));
    System.out.println(sumDigitsInRange(3));
    System.out.println(sumDigitsInRange(7));
    System.out.println(sumDigitsInRange(8));
    System.out.println(sumDigitsInRange(13));
  }
}