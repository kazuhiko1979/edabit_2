import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class very_hard_Sorting_in_R_Order_Part_I_147{
    public static List<Integer> order(int[] lst) {
        List<int[]> keySorted = new ArrayList<>();
        for (int i = 0; i < lst.length; i++){
            keySorted.add(new int[]{lst[i], i});
        }

        Collections.sort(keySorted, (a, b) -> Integer.compare(a[0], b[0]));
        List<Integer> result = new ArrayList<>();
        for (int[] pair : keySorted) {
            result.add(pair[1]);
        }

        return result;
    }
    public static void main(String[] args) {
        System.out.println(order(new int[]{1, 3, 3, 9, 8}));
        System.out.println(order(new int[]{9, 1, 4, 5, 4}));
        System.out.println(order(new int[]{1, 1, 1, 1, 1}));
        System.out.println(order(new int[]{1, 2, 0, 3, 7, 1, 11, 1, 2}));
        System.out.println(order(new int[]{1, -4, (int)5.5, -1, 4, (int)7.5}));
    }


}