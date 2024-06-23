import java.util.ArrayList;
import java.util.List;

public class very_hard_Dividing_into_Chunks_of_Maximum_Sum_N_166 {

    public static List<List<Integer>> divide(List<Integer> lst, int n) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();

        for (int i : lst) {
            if (sum(temp) + i > n){
                result.add(new ArrayList<>(temp));
                temp.clear();
                temp.add(i);
            } else {
                temp.add(i);
            }
        }
        if (!temp.isEmpty()) {
            result.add(new ArrayList<>(temp));
        }

        return result;
    }

    private static int sum(List<Integer> list) {
        int sum = 0;
        for (int i : list){
            sum += i;
        }
        return sum;
    }

    public static void main(String[] args) {
        List<Integer> list1 = List.of(1, 2, 3, 4, 1, 0, 2, 2);
        List<Integer> list2 = List.of(1, 0, 1, 1, -1, 0, 0);
        List<Integer> list3 = List.of(2, 1, 0, -1, 0, 0, 2, 1, 3);

        System.out.println(divide(list1, 5));  // [[1, 2], [3], [4, 1, 0], [2, 2]]
        System.out.println(divide(list2, 1));  // [[1, 0], [1], [1, -1, 0, 0]]
        System.out.println(divide(list3, 3));  // [[2, 1, 0, -1, 0, 0], [2, 1], [3]]
    }
}