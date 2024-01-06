import java.util.ArrayList;
import java.util.List;

public class very_hard_Sums_of_Powers_of_Two_128 {
    public static List<Integer> sums_of_powers_of_two(int n) {
        List<Integer> result = new ArrayList<>();
        int power = 0;

        while (n > 0) {
            if ((n & 1) == 1){
                result.add((int)Math.pow(2, power));
            }
            power++;
            n >>= 1;
        }
        return result;
    }


    public static void main(String[] args) {
            System.out.println(sums_of_powers_of_two(21)); // [1, 4, 16]
            System.out.println(sums_of_powers_of_two(8));  // [8]
            System.out.println(sums_of_powers_of_two(63)); // [1, 2, 4, 8, 16, 32]
            System.out.println(sums_of_powers_of_two(1));  // [1]
            System.out.println(sums_of_powers_of_two(556846320));
            // [16, 32, 64, 128, 1024, 2048, 16384, 32768, 1048576, 2097152, 16777216, 536870912]
        }
}